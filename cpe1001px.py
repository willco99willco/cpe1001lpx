import importlib.util
import sys

def import_cpe_file(file_path):
    try:
    
        spec = importlib.util.spec_from_file_location("cpe_module", file_path)
        cpe_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cpe_module)
        return cpe_module
    except Exception as e:
        print(f"Failed to import '{file_path}': {e}")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python cpe1001lpx.py <python_script> <cpe_file>")
        return

    python_script = sys.argv[1]
    cpe_file = sys.argv[2]

    try:
        
        imported_module = import_cpe_file(cpe_file)

        
        if imported_module:
            exec(open(python_script).read())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()