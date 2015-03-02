# #START_LICENSE###########################################################
#
#
# This file is part of the Environment for Tree Exploration program
# (ETE).  http://etetoolkit.org
#  
# ETE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# ETE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with ETE.  If not, see <http://www.gnu.org/licenses/>.
#
# 
#                     ABOUT THE ETE PACKAGE
#                     =====================
# 
# ETE is distributed under the GPL copyleft license (2008-2015).  
#
# If you make use of ETE in published work, please cite:
#
# Jaime Huerta-Cepas, Joaquin Dopazo and Toni Gabaldon.
# ETE: a python Environment for Tree Exploration. Jaime BMC
# Bioinformatics 2010,:24doi:10.1186/1471-2105-11-24
#
# Note that extra references to the specific methods implemented in 
# the toolkit may be available in the documentation. 
# 
# More info at http://etetoolkit.org. Contact: huerta@embl.de
#
# 
# #END_LICENSE#############################################################
#!/usr/bin/env python
import sys
import os
TOOLSPATH = os.path.realpath(os.path.split(os.path.realpath(__file__))[0])
#sys.path.insert(0, TOOLSPATH)
sys.path.insert(1, TOOLSPATH.replace("ete2/tools", ''))
#print sys.path

import argparse
import ete_split, ete_expand, ete_annotate, ete_ncbiquery, ete_view, ete_generate, ete_mod, ete_extract, ete_compare
from ete2.tools import common
from ete2.tools.common import log


"""
def ete_split(args):
    # bydups, bydist, name, find clsuters
def ete_expand(args):
    # polytomies 
def ete_extract(args):
    #dups, orthologs, partitions, edges, dist_matrix, ancestor, 
def ete_convert(args):
    # between newick formats, orthoxml, phyloxml
def ete_maptrees(args):
def ete_reconcile(args):
def ete_consense(args):
    # all observed splits    
def ete_fetch(args):
def ete_codeml(args):

"""            
            
def tree_iterator(args):        
    if not args.src_trees and not sys.stdin.isatty():
        log.debug("Reading trees from standard input...")
        args.src_trees = sys.stdin
    elif not args.src_trees:
        log.error("At least one tree is required as input (i.e --src_trees ) ")
        sys.exit(-1)
    
    for stree in args.src_trees:
        # CHECK WHAT is needed before process the main command, allows mods before analyses        
        yield stree
      
        
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        import phylobuild
        del sys.argv[1]
        phylobuild._main()
        return
        
    # CREATE REUSABLE PARSER OPTIONS
    
    # main args
    main_args_p = argparse.ArgumentParser(add_help=False)
    common.populate_main_args(main_args_p)
    # source tree args
    source_args_p = argparse.ArgumentParser(add_help=False)
    common.populate_source_args(source_args_p)
    # ref tree args
    ref_args_p = argparse.ArgumentParser(add_help=False)
    common.populate_ref_args(ref_args_p)
    # mod
    mod_args_p = argparse.ArgumentParser(add_help=False)
    ete_mod.populate_args(mod_args_p)
    # expand
    expand_args_p = argparse.ArgumentParser(add_help=False)
    ete_expand.populate_args(expand_args_p)
    # extract
    extract_args_p = argparse.ArgumentParser(add_help=False)
    ete_extract.populate_args(extract_args_p)
    # split
    split_args_p = argparse.ArgumentParser(add_help=False)
    ete_split.populate_args(split_args_p)


    # ADD SUBPROGRAM TO THE MAIN PARSER
    parser = argparse.ArgumentParser(description="",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subparser = parser.add_subparsers(title="AVAILABLE PROGRAMS")

    # - ANNOTATE -
    mod_args_pp = subparser.add_parser("mod", parents=[source_args_p, main_args_p, mod_args_p],
                                       description=ete_mod.DESC,
                                       formatter_class=argparse.RawDescriptionHelpFormatter)
    mod_args_pp.set_defaults(func=ete_mod.run)
    
    # - ANNOTATE -
    annotate_args_p = subparser.add_parser("annotate", parents=[source_args_p, main_args_p],
                                       description=ete_annotate.DESC,
                                       formatter_class=argparse.RawDescriptionHelpFormatter)
    annotate_args_p.set_defaults(func=ete_annotate.run)
    ete_annotate.populate_args(annotate_args_p)
    

    # - COMPARE -
    compare_args_p = subparser.add_parser("compare", parents=[source_args_p, mod_args_p, ref_args_p, main_args_p],
                                           description=ete_compare.DESC,
                                          formatter_class=argparse.RawDescriptionHelpFormatter)
    compare_args_p.set_defaults(func=ete_compare.run)
    ete_compare.populate_args(compare_args_p)

    # - VIEW -
    view_args_p = subparser.add_parser("view", parents=[source_args_p, mod_args_p, main_args_p],
                                        description=ete_view.DESC,
                                       formatter_class=argparse.RawDescriptionHelpFormatter)
    view_args_p.set_defaults(func=ete_view.run)
    ete_view.populate_args(view_args_p)
    

    # - NCBIQUERY -
    ncbi_args_p = subparser.add_parser("ncbiquery", parents=[main_args_p],
                                       description=ete_ncbiquery.DESC)
    ncbi_args_p.set_defaults(func=ete_ncbiquery.run)
    ete_ncbiquery.populate_args(ncbi_args_p)
    
    # - GENERATE -
    generate_args_p = subparser.add_parser("generate", parents=[source_args_p, main_args_p],
                                           description=ete_generate.DESC,
                                           formatter_class=argparse.RawDescriptionHelpFormatter)
    
    generate_args_p.set_defaults(func=ete_generate.run)
    ete_generate.populate_args(generate_args_p)

    # - build -
    generate_args_p = subparser.add_parser("build")
    

    # ===================
    #  EXECUTE PROGRAM
    # ===================
    
    args = parser.parse_args()
    
    LOG_LEVEL = args.verbosity 
    
    if hasattr(args, "src_trees"):
        args.src_tree_iterator = tree_iterator(args)
        
    elif hasattr(args, "search"):
        if not args.search and not sys.stdin.isatty():
            log.debug("Reading taxa from standard input...")
            args.search = sys.stdin 
        
    # Call main program
    args.func(args)

if __name__=="__main__":
    main()
