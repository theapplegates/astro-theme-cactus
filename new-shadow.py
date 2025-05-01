import json
import os
from urllib.parse import urlparse, urlunparse
import re
import argparse
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()  

def upload_to_cloudinary(image_path, responsive_breakpoints, shadow_params=None):
    """
    Uploads an image to Cloudinary and returns the response as a JSON object.
    
    Args:
        image_path: Path to the image file to upload
        responsive_breakpoints: Configuration for responsive breakpoints
        shadow_params: Optional shadow effect parameters
    
    Returns:
        dict: Cloudinary API response
    """
    # Check if required environment variables are set
    required_vars = ['CLOUDINARY_CLOUD_NAME', 'CLOUDINARY_API_KEY', 'CLOUDINARY_API_SECRET']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Configure Cloudinary with credentials
    cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET')
    )
    
    # Add shadow transformation if provided
    upload_options = {
        'responsive_breakpoints': responsive_breakpoints
    }
    
    # Add transformation for shadow if provided
    if shadow_params:
        upload_options['transformation'] = shadow_params
    
    try:
        print(f"Uploading image to Cloudinary...")
        response = cloudinary.uploader.upload(image_path, **upload_options)
        return response
    except cloudinary.exceptions.Error as e:
        raise Exception(f"Cloudinary upload failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Upload error: {str(e)}")

def modify_transformations(url, width, extra_transformation=None, dpr=None, shadow_params=None):
    """
    Modifies Cloudinary transformations in a URL to include width scaling,
    extra art direction transformations, DPR setting, and shadow effects.
    
    Args:
        url: The Cloudinary URL to modify
        width: The desired width for the image
        extra_transformation: Optional art direction transformation
        dpr: Optional device pixel ratio value
        shadow_params: Optional shadow effect parameters
    
    Returns:
        str: Modified Cloudinary URL
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    path_parts = path.split('/')

    try:
        upload_index = path_parts.index('upload')
    except ValueError:
        raise ValueError(f"Invalid Cloudinary URL: 'upload' not found in path: {url}")

    # Collect existing transformation parts (if any)
    transformations = []
    rest_of_path = []
    in_transformations = True
    for part in path_parts[upload_index + 1:]:
        if in_transformations:
            if part.startswith('v') and part[1:].isdigit():
                in_transformations = False
                rest_of_path.append(part)
            elif '.' in part and '/' not in part:
                in_transformations = False
                rest_of_path.append(part)
            else:
                transformations.append(part)
        else:
            rest_of_path.append(part)

    # If an extra art direction transformation is provided, prepend it.
    if extra_transformation:
        # Avoid duplicating the extra transformation if already present.
        if extra_transformation not in transformations:
            transformations.insert(0, extra_transformation)

    # Insert DPR if provided (e.g. "dpr_2.0"). Place it before the scaling.
    if dpr:
        dpr_transformation = f'dpr_{dpr}'
        if dpr_transformation not in transformations:
            # Insert after art direction if present, otherwise at the beginning
            insert_pos = 1 if extra_transformation else 0
            transformations.insert(insert_pos, dpr_transformation)

    # Ensure we have a width scaling transformation.
    width_transformation = f'c_scale,w_{width}'
    if not any(f'w_{width}' in t for t in transformations):
        transformations.append(width_transformation)
    
    # Add shadow parameters if provided and not already in transformations
    if shadow_params and shadow_params not in transformations:
        transformations.append(shadow_params)

    new_path_parts = path_parts[:upload_index + 1] + transformations + rest_of_path
    new_path = '/' + '/'.join(new_path_parts)
    new_parsed_url = parsed_url._replace(path=new_path)
    new_url = urlunparse(new_parsed_url)
    return new_url

def generate_responsive_html(cloudinary_data, formats, alt_text, picture_class="responsive-picture", 
                            art_configs=None, shadow_params=None):
    """
    Generates responsive HTML <picture> element with art direction.
    For each art direction breakpoint, generates separate <source> elements 
    per image format including both DPR 1.0 and 2.0 variants.
    
    Args:
        cloudinary_data: Response from Cloudinary upload
        formats: List of image formats to include
        alt_text: Alt text for the image
        picture_class: CSS class for the picture element
        art_configs: List of art direction configurations
        shadow_params: Shadow effect parameters
    
    Returns:
        str: HTML markup for responsive picture element
    """
    # Get the list of width breakpoints provided by Cloudinary.
    breakpoints = [bp for rb in cloudinary_data['responsive_breakpoints'] for bp in rb['breakpoints']]
    
    # Sort breakpoints by width (descending)
    breakpoints = sorted(breakpoints, key=lambda x: x['width'], reverse=True)

    # Use provided art configs or default if none provided
    if not art_configs:
        art_configs = [
            {
                "media": "(min-width: 1200px)",
                "sizes": "40vw",
                "extra_transformation": None  # Original aspect ratio
            },
            {
                "media": "(min-width: 992px) and (max-width: 1199px)",
                "sizes": "60vw",
                "extra_transformation": "ar_16:9,c_fill,g_auto"
            },
            {
                "media": "(min-width: 768px) and (max-width: 991px)",
                "sizes": "70vw",
                "extra_transformation": "ar_4:3,c_fill,g_auto"
            },
            {
                "media": "(max-width: 767px)",
                "sizes": "100vw",
                "extra_transformation": "ar_1:1,c_fill,g_auto"
            }
        ]

    html_output = f'<div class="shadow-wrapper">\n<picture class="{picture_class}">\n'
    for art in art_configs:
        for fmt in formats:
            html_output += f'  <source media="{art["media"]}" type="image/{fmt}" sizes="{art["sizes"]}"\n          srcset="\n'
            # For each breakpoint, output DPR 1.0 and DPR 2.0 URLs.
            for bp in breakpoints:
                width = bp['width']
                # DPR 1.0 variant
                url_dpr1 = modify_transformations(
                    bp['secure_url'], 
                    width,
                    extra_transformation=art["extra_transformation"],
                    dpr="1.0",
                    shadow_params=shadow_params
                )
                url_dpr1 = re.sub(r'\.[a-zA-Z0-9]+$', f'.{fmt}', url_dpr1)
                # DPR 2.0 variant (width effectively doubles)
                url_dpr2 = modify_transformations(
                    bp['secure_url'], 
                    width,
                    extra_transformation=art["extra_transformation"],
                    dpr="2.0",
                    shadow_params=shadow_params
                )
                url_dpr2 = re.sub(r'\.[a-zA-Z0-9]+$', f'.{fmt}', url_dpr2)
                html_output += f'    {url_dpr1} {width}w,\n'
                html_output += f'    {url_dpr2} {width * 2}w,\n'
            html_output = html_output.rstrip(',\n') + '\n  "/>\n'
    
    # Fallback <img> tag (using the last breakpoint of the original transformation)
    fallback_bp = breakpoints[-1]  # Smallest breakpoint for fallback
    fallback_url = modify_transformations(
        fallback_bp["secure_url"], 
        fallback_bp["width"],
        shadow_params=shadow_params
    )
    fallback_url = re.sub(r'\.[a-zA-Z0-9]+$', '.jpeg', fallback_url)  # default fallback format
    html_output += f'  <img src="{fallback_url}" alt="{alt_text}" loading="lazy">\n'
    html_output += '</picture>\n</div>'
    return html_output

def parse_shadow_params(shadow_string):
    """
    Parse shadow parameters string into Cloudinary transformation format.
    
    Args:
        shadow_string: String containing shadow parameters
        
    Returns:
        str: Formatted shadow parameter string
    """
    if not shadow_string:
        return None
    
    # If already in Cloudinary transformation format, return as is
    if shadow_string.startswith('e_shadow:'):
        return shadow_string
    
    # Otherwise, create formatted shadow parameter
    return f'e_shadow:{shadow_string}'

def main():
    """Main function to orchestrate the image upload and HTML generation."""
    parser = argparse.ArgumentParser(description="Upload image to Cloudinary and generate responsive HTML.")
    parser.add_argument("image_file", help="Path to the image file")
    parser.add_argument("--output", default="output.html", help="Path to the output HTML file")
    parser.add_argument("--alt", default="Responsive Image", help="Alt text for the image")
    parser.add_argument("--picture_class", default="responsive-picture", help="Class for the picture tag")
    parser.add_argument("--shadow", default="75,x_20,y_20", help="Shadow parameters (intensity,x_offset,y_offset)")
    parser.add_argument("--bytes_step", type=int, default=20000, help="Bytes step for responsive breakpoints")
    parser.add_argument("--min_width", type=int, default=250, help="Minimum width for responsive breakpoints")
    parser.add_argument("--max_width", type=int, default=1000, help="Maximum width for responsive breakpoints")
    parser.add_argument("--transformation_crop", default="fill", help="Transformation crop value")
    parser.add_argument("--transformation_gravity", default="auto", help="Transformation gravity value")
    parser.add_argument("--use_art_direction", action="store_true", help="Enable art direction for different screen sizes")
    
    args = parser.parse_args()

    # Image formats in order of preference (most efficient to most compatible)
    formats = ['jxl', 'avif', 'jpeg']
    output_html_file = args.output
    alt_text = args.alt
    picture_class = args.picture_class
    
    # Parse shadow parameters
    shadow_params = parse_shadow_params(args.shadow)

    # Configure responsive breakpoints for Cloudinary
    responsive_breakpoints = {
        "create_derived": True,
        "bytes_step": args.bytes_step,
        "min_width": args.min_width,
        "max_width": args.max_width,
        "transformation": {
            "crop": args.transformation_crop,
            "gravity": args.transformation_gravity,
        }
    }

    # Set up art direction configurations if enabled
    art_configs = None
    if args.use_art_direction:
        art_configs = [
            {
                "media": "(min-width: 1200px)",
                "sizes": "40vw",
                "extra_transformation": None  # Original aspect ratio
            },
            {
                "media": "(min-width: 992px) and (max-width: 1199px)",
                "sizes": "60vw",
                "extra_transformation": "ar_16:9,c_fill,g_auto"
            },
            {
                "media": "(min-width: 768px) and (max-width: 991px)",
                "sizes": "70vw",
                "extra_transformation": "ar_4:3,c_fill,g_auto"
            },
            {
                "media": "(max-width: 767px)",
                "sizes": "100vw",
                "extra_transformation": "ar_1:1,c_fill,g_auto"
            }
        ]

    try:
        # Check if image file exists
        if not os.path.exists(args.image_file):
            print(f"Error: Image file '{args.image_file}' not found")
            sys.exit(1)
            
        print(f"Uploading {args.image_file} to Cloudinary...")
        cloudinary_response = upload_to_cloudinary(args.image_file, responsive_breakpoints)
        print("Upload complete. Generating HTML...")

        html = generate_responsive_html(
            cloudinary_response, 
            formats, 
            alt_text, 
            picture_class,
            art_configs, 
            shadow_params
        )

        with open(output_html_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Responsive HTML written to {output_html_file}")

    except EnvironmentError as e:
        print(f"Environment error: {e}")
        print("Please check your .env file contains the required Cloudinary credentials.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
