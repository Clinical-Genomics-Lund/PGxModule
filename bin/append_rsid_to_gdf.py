#!/usr/bin/env python3

from get_target_variants import GDF
import argparse
import sys
from distutils.util import strtobool

# As script to run "shell:" in snakemake rule to allow singularity run


def main():
    parser = argparse.ArgumentParser(
        description="Rewrite bed to chr:start-end list. Removing wt targets or adding padding"
    )
    parser.add_argument("--input_gdf", type=str)
    parser.add_argument("--target_bed", type=str)
    parser.add_argument("--output_file", type=str)
    parser.add_argument(
        "--addchr",
        type=lambda x: bool(strtobool(x)),
        nargs="?",
        const=True,
        default=False,
        help="add chr to the chromosomes",
    )

    args = parser.parse_args(sys.argv[1:])

    input_gdf = args.input_gdf
    target_bed = args.target_bed
    output_file = args.output_file
    addchr = args.addchr
    print(args.addchr)

    c_gdf = GDF(input_gdf, addchr)
    c_gdf.rsid_per_position(target_bed)
    c_gdf.write_proccessed_gdf(output_file)


if __name__ == "__main__":
    main()
