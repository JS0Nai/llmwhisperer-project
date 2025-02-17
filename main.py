import sys
import os
import glob
from unstract.llmwhisperer import LLMWhispererClientV2
from dotenv import load_dotenv

def process_pdf(file_path):
    """Process a single PDF file using LLMWhisperer V2"""
    client = LLMWhispererClientV2()
    
    try:
        # Process with high quality settings and wait for completion
        result = client.whisper(
            file_path=file_path,
            mode='high_quality',                # Direct parameter
            output_mode='layout_preserving',    # Direct parameter
            mark_vertical_lines=True,           # Direct parameter
            mark_horizontal_lines=True,         # Direct parameter
            wait_for_completion=True,           # Makes it synchronous
            wait_timeout=600                    # 10 minutes timeout
        )
        
        # Extract and save the text
        if result.get("extraction") and result["extraction"].get("result_text"):
            output_dir = os.path.join(os.path.dirname(file_path), "extracted_text")
            os.makedirs(output_dir, exist_ok=True)
            
            output_file = os.path.join(output_dir, f"{os.path.basename(file_path)}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result["extraction"]["result_text"])
            
            print(f"✓ Successfully processed: {file_path}")
            print(f"  Saved to: {output_file}")
            return True
            
        else:
            print(f"✗ No text extracted from: {file_path}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("LLMWHISPERER_API_KEY"):
        print("Error: LLMWHISPERER_API_KEY not found in environment variables")
        sys.exit(1)
    
    # Get input path from command line
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pdf_or_directory>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    
    # Collect files to process
    files_to_process = []
    if os.path.isfile(input_path) and input_path.lower().endswith('.pdf'):
        files_to_process.append(input_path)
    elif os.path.isdir(input_path):
        files_to_process.extend(glob.glob(os.path.join(input_path, "*.pdf")))
    
    if not files_to_process:
        print(f"No PDF files found in {input_path}")
        sys.exit(1)
    
    # Process files
    print(f"\nFound {len(files_to_process)} PDF files to process")
    successful = 0
    
    for file_path in files_to_process:
        print(f"\nProcessing: {file_path}")
        if process_pdf(file_path):
            successful += 1
    
    # Summary
    print(f"\nProcessing complete: {successful}/{len(files_to_process)} files successful")

if __name__ == "__main__":
    main()