# kameris-experiments

[![Travis](https://travis-ci.org/stephensolis/kameris-experiments.svg?branch=master)](https://travis-ci.org/stephensolis/kameris-experiments)

This is a collection of datasets, job description files, and pre-trained models for use with [Kameris](https://github.com/stephensolis/kameris). <br>
By default, Kameris will attempt to find unknown dataset files and models from this repo, as described in `files.yml`.

## Coming from a paper?

If you came here from:

**"An open-source k-mer based machine learning tool for fast and accurate subtyping of HIV-1 genomes"**

See the experiments in the `hiv1` folder as well as `dengue`, `flu`, `hepatitis`.

**"Unravelling eukaryotic diversity with an alignment-free machine learning method"**

See the experiments in the `mmetsp` and `1kplants` folders.

## Citing

If you use any of the datasets or experiments with names starting with `hiv1`, `dengue`, `flu`, or `hepatitis` in your research, please cite:

**An open-source k-mer based machine learning tool for fast and accurate subtyping of HIV-1 genomes** <br>
Stephen Solis-Reyes, Mariano Avino, Art Poon, Lila Kari <br>
https://www.biorxiv.org/content/early/2018/07/05/362780

## Experiments

Any of the following experiments can be easily run as follows:
1. Visit https://github.com/stephensolis/kameris and follow the instructions to install Kameris.
2. Create an empty folder and open a terminal in the folder.
3. Create new folders `data` and `output`.
4. Run `kameris run-job https://raw.githubusercontent.com/stephensolis/kameris-experiments/master/experiments/[name of experiment].yml https://raw.githubusercontent.com/stephensolis/kameris/master/demo/settings.yml`

| Name | Description |
|---|---|
| `1kplants/1kplants` | Classify plant genomes into clade, order, and family, with different amounts of sampling per genome |
| `dengue/ncbi-whole` | Classify dengue virus genomes by subtype |
| `dna-types/mtdna-vs-plastid-vs-plasmid` | Classify whole organelle genomes by type: mitochondrial, plastid, and plasmid |
| `dna-types/mtdna-vs-plastid` | Classify whole organelle genomes by type: mitochondrial and plastid |
| `flu/ncbi-whole` | Classify influenza type A genomes by subtype, on different regions of the genome |
| `genomes-nuclear/5kingdoms` | Classify whole nuclear genomes by 5 of the 6 kingdoms: animals, archaea, bacteria, fungi, and plants |
| `genomes-nuclear/archaea` | Classify whole archaeal genomes into 3 phyla |
| `genomes-nuclear/bacteria` | Classify whole bacterial genomes into 4 phyla or 5 proteobacterial classes |
| `genomes-nuclear/fungi` | Classify whole fungal genomes into 3 phyla or subphyla |
| `genomes-nuclear/plants` | Classify whole plant genomes into 2 clades |
| `genomes-nuclear/vertebrates` | Classify whole vertebrate genomes into birds, fish, and mammals |
| `hepatitis/hbv-whole` | Classify whole hepatitis B genomes by subtype |
| `hepatitis/hcv-whole` | Classify whole hepatitis C genomes by subtype |
| `hiv1/lanl-pol` | Classify whole HIV-1 *pol* genes by subtype |
| `hiv1/lanl-reference-model` | Train the HIV-1 classifier on whole HIV-1 *pol* genes used in "An open-source k-mer based machine learning tool for fast and accurate subtyping of HIV-1 genomes" |
| `hiv1/lanl-whole` | Classify whole HIV-1 genomes by subtype |
| `hiv1/real-vs-synthetic` | Classify natural vs. synthetic HIV-1 *pol* genes |
| `hiv1/synthetic-pol` | Classify synthetic HIV-1 *pol* genes by subtype |
| `human-haplogroups/human-haplogroups` | Classify whole human mitochondrial genomes by haplogroup |
| `mmetsp/mmetsp-superphylum` | Classify marine microbial transcriptomes into superphylum, with different amounts of sampling per transcriptome |
| `mmetsp/mmetsp` | Classify marine microbial transcriptomes into phylum, class, order, family, and genus, with different amounts of sampling per transcriptome |
| `mtdna/amphibians` | Classify whole amphibian mitochondrial genomes into 3 orders |
| `mtdna/fungi` | Classify whole fungal mitochondrial genomes into 3 phyla/subphyla |
| `mtdna/insects-mammals-amphibians` | Classify whole animal mitochondrial genomes by class: insects, mammals, amphibians |
| `mtdna/insects` | Classify whole insect mitochondrial genomes into 7 insect orders/superorders |
| `mtdna/mammals` | Classify whole mammal mitochondrial genomes into 8 orders/superorders |
| `mtdna/plants-animals-fungi-protists` | Classify whole eukaryote mitochondrial genomes by kingdom: plants, animals, fungi, protists |
| `mtdna/plants` | Classify whole plant mitochondrial genomes into 2 clades |
| `mtdna/primates` | Classify whole primate mitochondrial genomes into 2 suborders |
| `mtdna/protists` | Classify whole protist mitochondrial genomes into 3 superphyla |
| `mtdna/vertebrates` | Classify whole vertebrate mitochondrial genomes into amphibians, birds, fish, mammals, and reptiles |
| `plasmids/bacteria` | Classify whole bacterial plasmid genomes into 4 phyla |
| `plasmids/proteobacteria` | Classify whole protobacterial plasmid genomes into 3 classes |
| `plastids/plants` | Classify whole plant plastid genomes into 5 clades |
| `plastids/protists` | Classify whole protist plastid genomes into 3 superphyla |
| `taxa/cpdna` | Classify whole choloroplast genomes from the same family or genus into genii or species |
| `taxa/mtdna` | Classify whole mitochondrial genomes from the same family or genus into genii or species |
| `viruses/dsDNA` | Classify whole dsDNA viral genomes by family |
| `viruses/groups` | Classify whole viral genomes by group |
| `viruses/retrotranscribing` | Classify whole retrotranscribing viral genomes by family |
| `viruses/satellites` | Classify whole satellite viral genomes by family |
| `viruses/ssDNA` | Classify whole ssDNA viral genomes by family |
| `viruses/ssRNAnegative` | Classify whole (-)ssRNA viral genomes by family |
| `viruses/ssRNApositive` | Classify whole (+)ssRNA viral genomes by family |

## Datasets

| Name | Description | Retrieval instructions | Retrieval date |
|---|---|---|---|
| `1kplants` | Plant genome assemblies | From the University of Alberta 1000 Plants (1kP) Initiative: metadata from http://www.onekp.com/samples/list.php and sequence data from http://www.onekp.com/public_data.html | N/A (static dataset) |
| `cpdna-all` | Whole chloroplast genomes | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `"chloroplast"[Title] AND "complete"[Title] AND "genome"[Title] NOT "gene"[Title] NOT "contig"[Title] NOT "scaffold"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "virus"[Title] NOT "plasmid"[Title] AND ("1000"[SLEN] : "999999999"[SLEN])`. Results were manually reviewed and some sequences which were not whole genomes were removed. | May 17, 2017 |
| `cpdna-taxa` | Whole chloroplast genomes, split into families/genii | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `"<taxonomy ID>"[Organism:exp] AND "chloroplast"[Title] AND "complete"[Title] AND "genome"[Title] NOT "gene"[Title] NOT "contig"[Title] NOT "scaffold"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "virus"[Title] NOT "plasmid"[Title] AND ("12000"[SLEN] : "99999999"[SLEN])` for every family with more than 50 sequence entries | March 13, 2017 |
| `dengue-ncbi-whole` | Whole dengue virus genomes | From the NCBI Virus Variation sequence database, https://www.ncbi.nlm.nih.gov/genomes/VirusVariation/Database/nph-select.cgi?taxid=12637 with query options "Nucleotide", "Full-length sequences only", and "Collapse identical sequences" | August 10, 2017 |
| `flu-ncbi` | Whole influenza genomes, split into genomic regions | From the NCBI Virus Variation sequence database, https://www.ncbi.nlm.nih.gov/genomes/FLU/Database/nph-select.cgi?go=genomeset with query options "Genome sets: Complete only", and "Type: A, B" | August 10, 2017 |
| `genomes-animals` | Whole assembled animal genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Group: Animals", "Levels: Complete, Chromosome" | June 15, 2017 |
| `genomes-archaea` | Whole assembled archaeal genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Kingdom: Archaea", "Levels: Complete, Chromosome" | June 24, 2017 |
| `genomes-bacteria` | Whole assembled bacterial genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Kingdom: Bacteria", "Levels: Complete, Chromosome" | June 25, 2017 |
| `genomes-fungi` | Whole assembled fungal genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Group: Fungi", "Levels: Complete, Chromosome" | June 24, 2017 |
| `genomes-plants` | Whole assembled plant genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Group: Plants", "Levels: Complete, Chromosome" | June 15, 2017 |
| `genomes-protists` | Whole assembled protist genomes | From the NCBI Genome browser, https://www.ncbi.nlm.nih.gov/genome/browse/ with query options "Group: Protists", "Levels: Complete, Chromosome" | June 15, 2017 |
| `hbv-ibcp-whole` | Whole hepatitis B genomes | From the Hepatitis B Virus Database operated by the Institut de Biologie et Chimie des Proteines (IBCP), https://hbvdb.ibcp.fr/HBVdb/HBVdbDataset?seqtype=0 | August 10, 2017 |
| `hcv-lanl-whole` | Whole hepatitis C genomes | From the Los Alamos (LANL) sequence database, https://hcv.lanl.gov/components/sequence/HCV/search/searchi.html, with query options "Excluding recombinants", "Excluding 'no genotype'", "Genomic region: complete genome", and "Excluding problematic" | August 10, 2017 |
| `hiv1-lanl-pol` | HIV-1 *pol* gene coding regions | From the Los Alamos (LANL) sequence database, https://www.hiv.lanl.gov/components/sequence/HIV/search/search.html with query options "Virus: HIV-1", "Genomic region: Pol CDS", "Excluding problematic" | Retrieved May 18, 2017, site reported update May 6, 2017 |
| `hiv1-lanl-whole` | Whole HIV-1 genomes | From the Los Alamos (LANL) sequence database, https://www.hiv.lanl.gov/components/sequence/HIV/search/search.html with query options "Virus: HIV-1", "Genomic region: complete genome", "Excluding problematic" | Retrieved May 18, 2017, site reported update May 6, 2017 |
| `hiv1-mixed-polfragments` | Natural HIV-1 *pol* gene fragments | The curated testing dataset described in "An open-source k-mer based machine learning tool for fast and accurate subtyping of HIV-1 genomes" | See paper |
| `hiv1-synthetic-polfragments` | Synthetically-generated HIV-1 *pol* gene fragments | Described in "An open-source k-mer based machine learning tool for fast and accurate subtyping of HIV-1 genomes" | See paper |
| `mmetsp` | Assembled marine eukaryote transcriptomes | From the Marine Microbial Eukaryote Transcriptome Sequencing Project (MMETSP): dataset information at https://www.imicrobe.us/#/projects/104 and data downloaded from ftp://ftp.imicrobe.us/projects/104/samples/ | N/A (static dataset) |
| `mtdna-all` | Whole mitochondrial genomes | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `("mitochondrial"[Title] OR "mitochondria"[Title] OR "mitochondrion"[Title]) AND "complete"[Title] AND "genome"[Title] NOT "gene"[Title] NOT "contig"[Title] NOT "scaffold"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "virus"[Title] NOT "plasmid"[Title] AND ("1000"[SLEN] : "999999999"[SLEN])`. Results were manually reviewed and some sequences which were not whole genomes were removed. | May 17, 2017 |
| `mtdna-human-haplogroups` | Whole human mitochondrial genomes | From the MITOMAP project (http://www.mitomap.org/MITOMAP/Mitobank), http://www.mitomap.org/foswiki/pub/MITOMAP/Mitobank/genbank_ids_2016June25.csv | Database date June 25, 2016 |
| `mtdna-refseq` | Whole mitochondrial genomes | From NCBI RefSeq release 81, ftp://ftp.ncbi.nlm.nih.gov/refseq/release/mitochondrion/ | RefSeq release date March 6, 2017 |
| `mtdna-taxa` | Whole mitochondrial genomes, split into families/genii | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `"<taxonomy ID>"[Organism:exp] AND ("mitochondrial"[Title] OR "mitochondria"[Title] OR "mitochondrion"[Title]) NOT "contig"[Title] NOT "scaffold"[Title] NOT "partial"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "incomplete"[Title] AND ("12000"[SLEN] : "99999999"[SLEN])` for every family with more than 30 sequence entries. For family *Hominidae*, every *Homo sapiens* sequence except NC_012920.1 and NC_011137.1 was omitted. | March 13, 2017 |
| `plasmids-all` | Whole plasmid genomes | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `"plasmid"[Title] AND "complete"[Title] NOT "gene"[Title] NOT "contig"[Title] NOT "scaffold"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "virus"[Title] NOT "coding"[Title] NOT "genes"[Title] NOT "pseudogene"[Title] NOT "protein"[Title] NOT "vector"[Title] NOT "operon"[Title] NOT "partial"[Title] NOT "transposon"[Title] NOT "rna"[Title] AND ("1000"[SLEN] : "999999999"[SLEN])`. Results were manually reviewed and some sequences which were not whole genomes were removed. | July 24, 2017 |
| `plasmids-refseq` | Whole plasmid genomes | From NCBI RefSeq release 83, ftp://ftp.ncbi.nlm.nih.gov/refseq/release/plasmid/ | RefSeq release date July 21, 2017 |
| `plastids-refseq` | Whole plastid genomes | From NCBI RefSeq release 82, ftp://ftp.ncbi.nlm.nih.gov/refseq/release/plastid/ | RefSeq release date May 15, 2017 |
| `viruses-all` | Whole viral genomes | From the NCBI Nucleotide database, https://www.ncbi.nlm.nih.gov/nucleotide/ with query `"txid10239"[Organism:exp] AND ("complete genome"[Title] OR "complete sequence"[Title]) NOT "miRNA"[Title] NOT "long terminal repeat"[Title] NOT "ltr"[Title] NOT "contig"[Title] NOT "spacer"[Title] NOT "pseudogene"[Title] NOT "genes"[Title] NOT "gene"[Title] NOT "segment"[Title] NOT "partial"[Title] NOT "cds"[Title] NOT "except"[Title] NOT "region"[Title] NOT "incomplete"[Title]`. Results were manually reviewed and some sequences which were not whole genomes were removed. | May 14, 2017 |
| `viruses-refseq` | Whole viral genomes | From NCBI RefSeq release 83, ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/ | RefSeq release date July 21, 2017 |

## Models

| Name | Description |
|---|---|
| `hiv1-linearsvm` | HIV-1 subtypes classifier, trained using experiment `hiv1/lanl-whole` with settings `k=6`, `include_recombinants=true`, `linear-svm` classifier |
| `hiv1-mlp` | HIV-1 subtypes classifier, trained using experiment `hiv1/lanl-whole` with settings `k=6`, `include_recombinants=true`, `multilayer-perceptron` classifier |

## License ![MIT](http://img.shields.io/:license-mit-blue.svg) ![CC0](http://img.shields.io/:license-CC0-green.svg)

The archives linked to in `files.yml` may contain copyrighted, proprietary, and/or confidential data. Use at your own risk.

The contents of this repository except for the `metadata/` directory are licensed as follows:

    The MIT License (MIT)

    Copyright (c) 2017 Stephen

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

## Training on new datasets
1. Clone https://github.com/stephensolis/kameris. Change 'urls_file' in kameris/utils/defaults.py to 'https://raw.githubusercontent.com/[your_git_id]/kameris-experiments/master/files.yml'.
2. Zip all sequences fasta files for training into a single zip file. Make sure the sequences are in the root of the archive, not inside a folder. Upload this zip to google drive. Create a new entry with the download url in 'archives' in files.yml. 
3. (Optional) Create another folder containing all sequences fasta files but all sequences files belonging to cluster 'A' are contained in a subfolder named 'A'. Give the folder the name 'sequences'. Put it into samples/. See samples/sequences. 
4. Open a json file and fill it in with the classes they belong to. id should be the name of the corresponding sequence file without the .fasta extension. If you have done Step 3, you can run `cd samples`, `python create_json.py sequences`, to get an idea of how the metadata file can be created. A file named 'sequences.json' should be created inside metadata/ folder.
5. Create an new entry with the download url in 'metadata' in files.yml.
6. Push all changes to your repo.
8. Create an 'experiment.yml' file. 
7. Open a terminal in the experiment folder and run `kameris run-job experiment.yml https://raw.githubusercontent.com/stephensolis/kameris/master/demo/settings.yml`.

This should give you results for k=4,5.

You can edit the experiment.yml file and keep an eye on these properties, for example:
1. k -- a list of values of k (inclusive) you want to run
2. validation_count -- accuracy is reported as N-fold cross-validation, this number is the value of N
3. groups/subtype -- the cluster names
4. classifiers -- name of classifiers to run

The contents of the `metadata/` directory are licensed as follows:

    CC0 1.0 Universal

    Statement of Purpose

    The laws of most jurisdictions throughout the world automatically confer
    exclusive Copyright and Related Rights (defined below) upon the creator and
    subsequent owner(s) (each and all, an "owner") of an original work of
    authorship and/or a database (each, a "Work").

    Certain owners wish to permanently relinquish those rights to a Work for the
    purpose of contributing to a commons of creative, cultural and scientific
    works ("Commons") that the public can reliably and without fear of later
    claims of infringement build upon, modify, incorporate in other works, reuse
    and redistribute as freely as possible in any form whatsoever and for any
    purposes, including without limitation commercial purposes. These owners may
    contribute to the Commons to promote the ideal of a free culture and the
    further production of creative, cultural and scientific works, or to gain
    reputation or greater distribution for their Work in part through the use and
    efforts of others.

    For these and/or other purposes and motivations, and without any expectation
    of additional consideration or compensation, the person associating CC0 with a
    Work (the "Affirmer"), to the extent that he or she is an owner of Copyright
    and Related Rights in the Work, voluntarily elects to apply CC0 to the Work
    and publicly distribute the Work under its terms, with knowledge of his or her
    Copyright and Related Rights in the Work and the meaning and intended legal
    effect of CC0 on those rights.

    1. Copyright and Related Rights. A Work made available under CC0 may be
    protected by copyright and related or neighboring rights ("Copyright and
    Related Rights"). Copyright and Related Rights include, but are not limited
    to, the following:

      i. the right to reproduce, adapt, distribute, perform, display, communicate,
      and translate a Work;

      ii. moral rights retained by the original author(s) and/or performer(s);

      iii. publicity and privacy rights pertaining to a person's image or likeness
      depicted in a Work;

      iv. rights protecting against unfair competition in regards to a Work,
      subject to the limitations in paragraph 4(a), below;

      v. rights protecting the extraction, dissemination, use and reuse of data in
      a Work;

      vi. database rights (such as those arising under Directive 96/9/EC of the
      European Parliament and of the Council of 11 March 1996 on the legal
      protection of databases, and under any national implementation thereof,
      including any amended or successor version of such directive); and

      vii. other similar, equivalent or corresponding rights throughout the world
      based on applicable law or treaty, and any national implementations thereof.

    2. Waiver. To the greatest extent permitted by, but not in contravention of,
    applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
    unconditionally waives, abandons, and surrenders all of Affirmer's Copyright
    and Related Rights and associated claims and causes of action, whether now
    known or unknown (including existing as well as future claims and causes of
    action), in the Work (i) in all territories worldwide, (ii) for the maximum
    duration provided by applicable law or treaty (including future time
    extensions), (iii) in any current or future medium and for any number of
    copies, and (iv) for any purpose whatsoever, including without limitation
    commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes
    the Waiver for the benefit of each member of the public at large and to the
    detriment of Affirmer's heirs and successors, fully intending that such Waiver
    shall not be subject to revocation, rescission, cancellation, termination, or
    any other legal or equitable action to disrupt the quiet enjoyment of the Work
    by the public as contemplated by Affirmer's express Statement of Purpose.

    3. Public License Fallback. Should any part of the Waiver for any reason be
    judged legally invalid or ineffective under applicable law, then the Waiver
    shall be preserved to the maximum extent permitted taking into account
    Affirmer's express Statement of Purpose. In addition, to the extent the Waiver
    is so judged Affirmer hereby grants to each affected person a royalty-free,
    non transferable, non sublicensable, non exclusive, irrevocable and
    unconditional license to exercise Affirmer's Copyright and Related Rights in
    the Work (i) in all territories worldwide, (ii) for the maximum duration
    provided by applicable law or treaty (including future time extensions), (iii)
    in any current or future medium and for any number of copies, and (iv) for any
    purpose whatsoever, including without limitation commercial, advertising or
    promotional purposes (the "License"). The License shall be deemed effective as
    of the date CC0 was applied by Affirmer to the Work. Should any part of the
    License for any reason be judged legally invalid or ineffective under
    applicable law, such partial invalidity or ineffectiveness shall not
    invalidate the remainder of the License, and in such case Affirmer hereby
    affirms that he or she will not (i) exercise any of his or her remaining
    Copyright and Related Rights in the Work or (ii) assert any associated claims
    and causes of action with respect to the Work, in either case contrary to
    Affirmer's express Statement of Purpose.

    4. Limitations and Disclaimers.

      a. No trademark or patent rights held by Affirmer are waived, abandoned,
      surrendered, licensed or otherwise affected by this document.

      b. Affirmer offers the Work as-is and makes no representations or warranties
      of any kind concerning the Work, express, implied, statutory or otherwise,
      including without limitation warranties of title, merchantability, fitness
      for a particular purpose, non infringement, or the absence of latent or
      other defects, accuracy, or the present or absence of errors, whether or not
      discoverable, all to the greatest extent permissible under applicable law.

      c. Affirmer disclaims responsibility for clearing rights of other persons
      that may apply to the Work or any use thereof, including without limitation
      any person's Copyright and Related Rights in the Work. Further, Affirmer
      disclaims responsibility for obtaining any necessary consents, permissions
      or other rights required for any use of the Work.

      d. Affirmer understands and acknowledges that Creative Commons is not a
      party to this document and has no duty or obligation with respect to this
      CC0 or use of the Work.
