# v2.1.0
- Updated Pharmcat Version to v3.2.0, which fixes a DYPD allele matcher bug 

# v2.0.4
- Corrected TMPT --> TPMT in the report header table

# v2.0.3
   - Updated sentieon certificates
   - haplotyping process now gives unzipped version of vcf files

# v2.0.2
   - Fixed Zero divison error when there is no allele depth in the variant calls (#43)
# v2.0.1
   - Updated Config
   - Fixed Pharmacat memory bug

# v2.0.0
   - Major change to the process flow
   - Updated pharmact to v2.12.0
   - Updated ReadMe.md

# v1.1.1
   - Updated QC text in the report

# v1.1.0
   - Added pharmCAT module to the pipeline

# v1.0.2
   - Updated DPYD HapB3 haplotype related rsids (rs75017182 and rs56038477)
   - Main target bed regions are padded with 20bp up and down stream
  
# v1.0.1
   - The report will now include a telephone number for medical information support related to its contents.

# v1.0.0
1. Added and updated various features:
   - Added license and workflow image.
   - Implemented nf-core style stubs.
   - Completed modularization of the pipeline with external arguments, singularity images, and configs.
   - Introduced panel/WGS profiles.
   - Addressed issues with variant calling for multiple samples and parallelization.
2. Variant calling and analysis improvements:
   - Added variant calling with SENTIEON/GATK, including variant filtration and annotation.
3. Important updates and fixes:
   - Corrected the NUDT15-3 rsID issue.
   - Updated recipe files and references for HG38 in configs, improving variant filtration.
4. Various report enhancements:
   - Fixed report warnings and updated report generation logic.
   - Improved report format, including a new logo, CSS updates, and added a gene table.
   - Added quality control comments and sample-specific MultiQC reporting.
   - Introduced a new Python-based reporting module, replacing the older R-based module.
