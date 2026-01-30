import os

def filter_genomes(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for genome in os.listdir(input_dir):
        if genome.endswith(".fna"):
            print(f"Processing {genome}")
            # Placeholder for QC filtering logic

if __name__ == "__main__":
    filter_genomes("example_data/", "filtered_genomes/")
