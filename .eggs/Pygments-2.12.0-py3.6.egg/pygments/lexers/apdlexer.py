"""
    pygments.lexers.apdlexer
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for ANSYS Parametric Design Language.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, words
from pygments.token import Comment, Keyword, Name, Text, Number, Operator, \
    String, Generic, Punctuation, Whitespace

__all__ = ['apdlexer']


class apdlexer(RegexLexer):
    """
    For APDL source code.

    .. versionadded:: 2.9
    """
    name = 'ANSYS parametric design language'
    aliases = ['ansys', 'apdl']
    filenames = ['*.ans']
    flags = re.IGNORECASE

    # list of elements
    elafunb = ("SURF152", "SURF153", "SURF154", "SURF156", "SHELL157",
               "SURF159", "LINK160", "BEAM161", "PLANE162",
               "SHELL163", "SOLID164", "COMBI165", "MASS166",
               "LINK167", "SOLID168", "TARGE169", "TARGE170",
               "CONTA171", "CONTA172", "CONTA173", "CONTA174",
               "CONTA175", "CONTA176", "CONTA177", "CONTA178",
               "PRETS179", "LINK180", "SHELL181", "PLANE182",
               "PLANE183", "MPC184", "SOLID185", "SOLID186",
               "SOLID187", "BEAM188", "BEAM189", "SOLSH190",
               "INTER192", "INTER193", "INTER194", "INTER195",
               "MESH200", "FOLLW201", "INTER202", "INTER203",
               "INTER204", "INTER205", "SHELL208", "SHELL209",
               "CPT212", "CPT213", "COMBI214", "CPT215", "CPT216",
               "CPT217", "FLUID220", "FLUID221", "PLANE223",
               "SOLID226", "SOLID227", "PLANE230", "SOLID231",
               "SOLID232", "PLANE233", "SOLID236", "SOLID237",
               "PLANE238", "SOLID239", "SOLID240", "HSFLD241",
               "HSFLD242", "SURF251", "SURF252", "REINF263",
               "REINF264", "REINF265", "SOLID272", "SOLID273",
               "SOLID278", "SOLID279", "SHELL281", "SOLID285",
               "PIPE288", "PIPE289", "ELBOW290", "USER300", "BEAM3",
               "BEAM4", "BEAM23", "BEAM24", "BEAM44", "BEAM54",
               "COMBIN7", "FLUID79", "FLUID80", "FLUID81", "FLUID141",
               "FLUID142", "INFIN9", "INFIN47", "PLANE13", "PLANE25",
               "PLANE42", "PLANE53", "PLANE67", "PLANE82", "PLANE83",
               "PLANE145", "PLANE146", "CONTAC12", "CONTAC52",
               "LINK1", "LINK8", "LINK10", "LINK32", "PIPE16",
               "PIPE17", "PIPE18", "PIPE20", "PIPE59", "PIPE60",
               "SHELL41", "SHELL43", "SHELL57", "SHELL63", "SHELL91",
               "SHELL93", "SHELL99", "SHELL150", "SOLID5", "SOLID45",
               "SOLID46", "SOLID65", "SOLID69", "SOLID92", "SOLID95",
               "SOLID117", "SOLID127", "SOLID128", "SOLID147",
               "SOLID148", "SOLID191", "VISCO88", "VISCO89",
               "VISCO106", "VISCO107", "VISCO108", "TRANS109")

    elafunc = ("PGRAPH", "/VT", "VTIN", "VTRFIL", "VTTEMP", "PGRSET",
               "VTCLR", "VTMETH", "VTRSLT", "VTVMOD", "PGSELE",
               "VTDISC", "VTMP", "VTSEC", "PGWRITE", "VTEVAL", "VTOP",
               "VTSFE", "POUTRES", "VTFREQ", "VTPOST", "VTSL",
               "FLDATA1-40", "HFPCSWP", "MSDATA", "MSVARY", "QFACT",
               "FLOCHECK", "HFPOWER", "MSMASS", "PERI", "SPADP",
               "FLREAD", "HFPORT", "MSMETH", "PLFSS", "SPARM",
               "FLOTRAN", "HFSCAT", "MSMIR", "PLSCH", "SPFSS",
               "HFADP", "ICE", "MSNOMF", "PLSYZ", "SPICE", "HFARRAY",
               "ICEDELE", "MSPROP", "PLTD", "SPSCAN", "HFDEEM",
               "ICELIST", "MSQUAD", "PLTLINE", "SPSWP", "HFEIGOPT",
               "ICVFRC", "MSRELAX", "PLVFRC", "HFEREFINE", "LPRT",
               "MSSOLU", "/PICE", "HFMODPRT", "MSADV", "MSSPEC",
               "PLWAVE", "HFPA", "MSCAP", "MSTERM", "PRSYZ")

    elafund = ("*VOPER", "VOVLAP", "*VPLOT", "VPLOT", "VPTN", "*VPUT",
               "VPUT", "*VREAD", "VROTAT", "VSBA", "VSBV", "VSBW",
               "/VSCALE", "*VSCFUN", "VSEL", "VSLA", "*VSTAT", "VSUM",
               "VSWEEP", "VSYMM", "VTRAN", "VTYPE", "/VUP", "*VWRITE",
               "/WAIT", "WAVES", "WERASE", "WFRONT", "/WINDOW",
               "WMID", "WMORE", "WPAVE", "WPCSYS", "WPLANE", "WPOFFS",
               "WPROTA", "WPSTYL", "WRFULL", "WRITE", "WRITEMAP",
               "*WRK", "WSORT", "WSPRINGS", "WSTART", "WTBCREATE",
               "XFDATA", "XFENRICH", "XFLIST", "/XFRM", "/XRANGE",
               "XVAR", "/YRANGE", "/ZOOM", "/WB", "XMLO", "/XML",
               "CNTR", "EBLOCK", "CMBLOCK", "NBLOCK", "/TRACK",
               "CWZPLOT", "~EUI", "NELE", "EALL", "NALL", "FLITEM",
               "LSLN", "PSOLVE", "ASLN", "/VERIFY", "/SSS", "~CFIN",
               "*EVAL", "*MOONEY", "/RUNSTAT", "ALPFILL",
               "ARCOLLAPSE", "ARDETACH", "ARFILL", "ARMERGE",
               "ARSPLIT", "FIPLOT", "GAPFINISH", "GAPLIST",
               "GAPMERGE", "GAPOPT", "GAPPLOT", "LNCOLLAPSE",
               "LNDETACH", "LNFILL", "LNMERGE", "LNSPLIT", "PCONV",
               "PLCONV", "PEMOPTS", "PEXCLUDE", "PINCLUDE", "PMETH",
               "/PMETH", "PMOPTS", "PPLOT", "PPRANGE", "PRCONV",
               "PRECISION", "RALL", "RFILSZ", "RITER", "RMEMRY",
               "RSPEED", "RSTAT", "RTIMST", "/RUNST", "RWFRNT",
               "SARPLOT", "SHSD", "SLPPLOT", "SLSPLOT", "VCVFILL",
               "/OPT", "OPEQN", "OPFACT", "OPFRST", "OPGRAD",
               "OPKEEP", "OPLOOP", "OPPRNT", "OPRAND", "OPSUBP",
               "OPSWEEP", "OPTYPE", "OPUSER", "OPVAR", "OPADD",
               "OPCLR", "OPDEL", "OPMAKE", "OPSEL", "OPANL", "OPDATA",
               "OPRESU", "OPSAVE", "OPEXE", "OPLFA", "OPLGR",
               "OPLIST", "OPLSW", "OPRFA", "OPRGR", "OPRSW",
               "PILECALC", "PILEDISPSET", "PILEGEN", "PILELOAD",
               "PILEMASS", "PILERUN", "PILESEL", "PILESTIF",
               "PLVAROPT", "PRVAROPT", "TOCOMP", "TODEF", "TOFREQ",
               "TOTYPE", "TOVAR", "TOEXE", "TOLOOP", "TOGRAPH",
               "TOLIST", "TOPLOT", "TOPRINT", "TOSTAT", "TZAMESH",
               "TZDELE", "TZEGEN", "XVAROPT", "PGSAVE", "SOLCONTROL",
               "TOTAL", "VTGEOM", "VTREAL", "VTSTAT")

    elafune = ("/ANUM", "AOFFST", "AOVLAP", "APLOT", "APPEND", "APTN",
               "ARCLEN", "ARCTRM", "AREAS", "AREFINE", "AREMESH",
               "AREVERSE", "AROTAT", "ARSCALE", "ARSYM", "ASBA",
               "ASBL", "ASBV", "ASBW", "ASCRES", "ASEL", "ASIFILE",
               "*ASK", "ASKIN", "ASLL", "ASLV", "ASOL", "/ASSIGN",
               "ASUB", "ASUM", "ATAN", "ATRAN", "ATYPE", "/AUTO",
               "AUTOTS", "/AUX2", "/AUX3", "/AUX12", "/AUX15",
               "AVPRIN", "AVRES", "AWAVE", "/AXLAB", "*AXPY",
               "/BATCH", "BCSOPTION", "BETAD", "BF", "BFA", "BFADELE",
               "BFALIST", "BFCUM", "BFDELE", "BFE", "BFECUM",
               "BFEDELE", "BFELIST", "BFESCAL", "BFINT", "BFK",
               "BFKDELE", "BFKLIST", "BFL", "BFLDELE", "BFLIST",
               "BFLLIST", "BFSCALE", "BFTRAN", "BFUNIF", "BFV",
               "BFVDELE", "BFVLIST", "BIOOPT", "BIOT", "BLC4", "BLC5",
               "BLOCK", "BOOL", "BOPTN", "BSAX", "BSMD", "BSM1",
               "BSM2", "BSPLIN", "BSS1", "BSS2", "BSTE", "BSTQ",
               "BTOL", "BUCOPT", "C", "CALC", "CAMPBELL", "CBDOF",
               "CBMD", "CBMX", "CBTE", "CBTMP", "CDOPT", "CDREAD",
               "CDWRITE", "CE", "CECHECK", "CECMOD", "CECYC",
               "CEDELE", "CEINTF", "CELIST", "CENTER", "CEQN",
               "CERIG", "CESGEN", "CFACT", "*CFCLOS", "*CFOPEN",
               "*CFWRITE", "/CFORMAT", "CGLOC", "CGOMGA", "CGROW",
               "CHECK", "CHKMSH", "CINT", "CIRCLE", "CISOL",
               "/CLABEL", "/CLEAR", "CLOCAL", "CLOG", "/CLOG",
               "CLRMSHLN", "CM", "CMACEL", "/CMAP", "CMATRIX",
               "CMDELE", "CMDOMEGA", "CMEDIT", "CMGRP", "CMLIST",
               "CMMOD", "CMOMEGA", "CMPLOT", "CMROTATE", "CMSEL",
               "CMSFILE", "CMSOPT", "CMWRITE", "CNCHECK", "CNKMOD",
               "CNTR", "CNVTOL", "/COLOR", "/COM", "*COMP", "COMBINE",
               "COMPRESS", "CON4", "CONE", "/CONFIG", "CONJUG",
               "/CONTOUR", "/COPY", "CORIOLIS", "COUPLE", "COVAL",
               "CP", "CPCYC", "CPDELE", "CPINTF", "/CPLANE", "CPLGEN",
               "CPLIST", "CPMERGE", "CPNGEN", "CPSGEN", "CQC",
               "*CREATE", "CRPLIM", "CS", "CSCIR", "CSDELE", "CSKP",
               "CSLIST", "CSWPLA", "CSYS", "/CTYPE", "CURR2D",
               "CUTCONTROL", "/CVAL", "CVAR", "/CWD", "CYCCALC",
               "/CYCEXPAND", "CYCFILES", "CYCFREQ", "*CYCLE",
               "CYCLIC", "CYCOPT", "CYCPHASE", "CYCSPEC", "CYL4",
               "CYL5", "CYLIND", "CZDEL", "CZMESH", "D", "DA",
               "DADELE", "DALIST", "DAMORPH", "DATA", "DATADEF",
               "DCGOMG", "DCUM", "DCVSWP", "DDASPEC", "DDELE",
               "DDOPTION", "DEACT", "DEFINE", "*DEL", "DELETE",
               "/DELETE", "DELTIM", "DEMORPH", "DERIV", "DESIZE",
               "DESOL", "DETAB", "/DEVDISP", "/DEVICE", "/DFLAB",
               "DFLX", "DFSWAVE", "DIG", "DIGIT", "*DIM",
               "/DIRECTORY", "DISPLAY", "/DIST", "DJ", "DJDELE",
               "DJLIST", "DK", "DKDELE", "DKLIST", "DL", "DLDELE",
               "DLIST", "DLLIST", "*DMAT", "DMOVE", "DMPEXT",
               "DMPOPTION", "DMPRAT", "DMPSTR", "DNSOL", "*DO", "DOF",
               "DOFSEL", "DOMEGA", "*DOT", "*DOWHILE", "DSCALE",
               "/DSCALE", "DSET", "DSPOPTION", "DSUM", "DSURF",
               "DSYM", "DSYS", "DTRAN", "DUMP", "/DV3D", "DVAL",
               "DVMORPH", "DYNOPT", "E", "EALIVE", "EDADAPT", "EDALE",
               "EDASMP", "EDBOUND", "EDBX", "EDBVIS", "EDCADAPT",
               "EDCGEN", "EDCLIST", "EDCMORE", "EDCNSTR", "EDCONTACT",
               "EDCPU", "EDCRB", "EDCSC", "EDCTS", "EDCURVE",
               "EDDAMP", "EDDBL", "EDDC", "EDDRELAX", "EDDUMP",
               "EDELE", "EDENERGY", "EDFPLOT", "EDGCALE", "/EDGE",
               "EDHGLS", "EDHIST", "EDHTIME", "EDINT", "EDIPART",
               "EDIS", "EDLCS", "EDLOAD", "EDMP", "EDNB", "EDNDTSD",
               "EDNROT", "EDOPT", "EDOUT", "EDPART", "EDPC", "EDPL",
               "EDPVEL", "EDRC", "EDRD", "EDREAD", "EDRI", "EDRST",
               "EDRUN", "EDSHELL", "EDSOLV", "EDSP", "EDSTART",
               "EDTERM", "EDTP", "EDVEL", "EDWELD", "EDWRITE",
               "EEXTRUDE", "/EFACET", "EGEN", "*EIGEN", "EINFIN",
               "EINTF", "EKILL", "ELBOW", "ELEM", "ELIST", "*ELSE",
               "*ELSEIF", "EMAGERR", "EMATWRITE", "EMF", "EMFT",
               "EMID", "EMIS", "EMODIF", "EMORE", "EMSYM", "EMTGEN",
               "EMUNIT", "EN", "*END", "*ENDDO", "*ENDIF",
               "ENDRELEASE", "ENERSOL", "ENGEN", "ENORM", "ENSYM",
               "EORIENT", "EPLOT", "EQSLV", "ERASE", "/ERASE",
               "EREAD", "EREFINE", "EREINF", "ERESX", "ERNORM",
               "ERRANG", "ESCHECK", "ESEL", "/ESHAPE", "ESIZE",
               "ESLA", "ESLL", "ESLN", "ESLV", "ESOL", "ESORT",
               "ESSOLV", "ESTIF", "ESURF", "ESYM", "ESYS", "ET",
               "ETABLE", "ETCHG", "ETCONTROL", "ETDELE", "ETLIST",
               "ETYPE", "EUSORT", "EWRITE", "*EXIT", "/EXIT", "EXP",
               "EXPAND", "/EXPAND", "EXPASS", "*EXPORT", "EXPROFILE",
               "EXPSOL", "EXTOPT", "EXTREM", "EXUNIT", "F", "/FACET",
               "FATIGUE", "FC", "FCCHECK", "FCDELE", "FCLIST", "FCUM",
               "FCTYP", "FDELE", "/FDELE", "FE", "FEBODY", "FECONS",
               "FEFOR", "FELIST", "FESURF", "*FFT", "FILE",
               "FILEAUX2", "FILEAUX3", "FILEDISP", "FILL", "FILLDATA",
               "/FILNAME", "FINISH", "FITEM", "FJ", "FJDELE",
               "FJLIST", "FK", "FKDELE", "FKLIST", "FL", "FLIST",
               "FLLIST", "FLST", "FLUXV", "FLUREAD", "FMAGBC",
               "FMAGSUM", "/FOCUS", "FOR2D", "FORCE", "FORM",
               "/FORMAT", "FP", "FPLIST", "*FREE", "FREQ", "FRQSCL",
               "FS", "FSCALE", "FSDELE", "FSLIST", "FSNODE", "FSPLOT",
               "FSSECT", "FSSPARM", "FSUM", "FTCALC", "FTRAN",
               "FTSIZE", "FTWRITE", "FTYPE", "FVMESH", "GAP", "GAPF",
               "GAUGE", "GCDEF", "GCGEN", "/GCMD", "/GCOLUMN",
               "GENOPT", "GEOM", "GEOMETRY", "*GET", "/GFILE",
               "/GFORMAT", "/GLINE", "/GMARKER", "GMATRIX", "GMFACE",
               "*GO", "/GO", "/GOLIST", "/GOPR", "GP", "GPDELE",
               "GPLIST", "GPLOT", "/GRAPHICS", "/GRESUME", "/GRID",
               "/GROPT", "GRP", "/GRTYP", "/GSAVE", "GSBDATA",
               "GSGDATA", "GSLIST", "GSSOL", "/GST", "GSUM", "/GTHK",
               "/GTYPE", "HARFRQ", "/HBC", "HBMAT", "/HEADER", "HELP",
               "HELPDISP", "HEMIOPT", "HFANG", "HFSYM", "HMAGSOLV",
               "HPGL", "HPTCREATE", "HPTDELETE", "HRCPLX", "HREXP",
               "HROPT", "HROCEAN", "HROUT", "IC", "ICDELE", "ICLIST",
               "/ICLWID", "/ICSCALE", "*IF", "IGESIN", "IGESOUT",
               "/IMAGE", "IMAGIN", "IMESH", "IMMED", "IMPD",
               "INISTATE", "*INIT", "/INPUT", "/INQUIRE", "INRES",
               "INRTIA", "INT1", "INTSRF", "IOPTN", "IRLF", "IRLIST",
               "*ITENGINE", "JPEG", "JSOL", "K", "KATT", "KBC",
               "KBETW", "KCALC", "KCENTER", "KCLEAR", "KDELE",
               "KDIST", "KEEP", "KESIZE", "KEYOPT", "KEYPTS", "KEYW",
               "KFILL", "KGEN", "KL", "KLIST", "KMESH", "KMODIF",
               "KMOVE", "KNODE", "KPLOT", "KPSCALE", "KREFINE",
               "KSCALE", "KSCON", "KSEL", "KSLL", "KSLN", "KSUM",
               "KSYMM", "KTRAN", "KUSE", "KWPAVE", "KWPLAN", "L",
               "L2ANG", "L2TAN", "LANG", "LARC", "/LARC", "LAREA",
               "LARGE", "LATT", "LAYER", "LAYERP26", "LAYLIST",
               "LAYPLOT", "LCABS", "LCASE", "LCCALC", "LCCAT",
               "LCDEF", "LCFACT", "LCFILE", "LCLEAR", "LCOMB",
               "LCOPER", "LCSEL", "LCSL", "LCSUM", "LCWRITE",
               "LCZERO", "LDELE", "LDIV", "LDRAG", "LDREAD", "LESIZE",
               "LEXTND", "LFILLT", "LFSURF", "LGEN", "LGLUE",
               "LGWRITE", "/LIGHT", "LINA", "LINE", "/LINE", "LINES",
               "LINL", "LINP", "LINV", "LIST", "*LIST", "LLIST",
               "LMATRIX", "LMESH", "LNSRCH", "LOCAL", "LOVLAP",
               "LPLOT", "LPTN", "LREFINE", "LREVERSE", "LROTAT",
               "LSBA", "*LSBAC", "LSBL", "LSBV", "LSBW", "LSCLEAR",
               "LSDELE", "*LSDUMP", "LSEL", "*LSENGINE", "*LSFACTOR",
               "LSLA", "LSLK", "LSOPER", "/LSPEC", "LSREAD",
               "*LSRESTORE", "LSSCALE", "LSSOLVE", "LSTR", "LSUM",
               "LSWRITE", "/LSYMBOL", "LSYMM", "LTAN", "LTRAN",
               "LUMPM", "LVSCALE", "LWPLAN", "M", "MADAPT", "MAGOPT",
               "MAGSOLV", "/MAIL", "MAP", "/MAP", "MAP2DTO3D",
               "MAPSOLVE", "MAPVAR", "MASTER", "MAT", "MATER",
               "MCHECK", "MDAMP", "MDELE", "MDPLOT", "MEMM", "/MENU",
               "MESHING", "MFANALYSIS", "MFBUCKET", "MFCALC", "MFCI",
               "MFCLEAR", "MFCMMAND", "MFCONV", "MFDTIME", "MFELEM",
               "MFEM", "MFEXTER", "MFFNAME", "MFFR", "MFIMPORT",
               "MFINTER", "MFITER", "MFLCOMM", "MFLIST", "MFMAP",
               "MFORDER", "MFOUTPUT", "*MFOURI", "MFPSIMUL", "MFRC",
               "MFRELAX", "MFRSTART", "MFSORDER", "MFSURFACE",
               "MFTIME", "MFTOL", "*MFUN", "MFVOLUME", "MFWRITE",
               "MGEN", "MIDTOL", "/MKDIR", "MLIST", "MMASS", "MMF",
               "MODCONT", "MODE", "MODIFY", "MODMSH", "MODSELOPTION",
               "MODOPT", "MONITOR", "*MOPER", "MOPT", "MORPH", "MOVE",
               "MP", "MPAMOD", "MPCHG", "MPCOPY", "MPDATA", "MPDELE",
               "MPDRES", "/MPLIB", "MPLIST", "MPPLOT", "MPREAD",
               "MPRINT", "MPTEMP", "MPTGEN", "MPTRES", "MPWRITE",
               "/MREP", "MSAVE", "*MSG", "MSHAPE", "MSHCOPY",
               "MSHKEY", "MSHMID", "MSHPATTERN", "MSOLVE", "/MSTART",
               "MSTOLE", "*MULT", "*MWRITE", "MXPAND", "N", "NANG",
               "NAXIS", "NCNV", "NDELE", "NDIST", "NDSURF", "NEQIT",
               "/NERR", "NFORCE", "NGEN", "NKPT", "NLADAPTIVE",
               "NLDIAG", "NLDPOST", "NLGEOM", "NLHIST", "NLIST",
               "NLMESH", "NLOG", "NLOPT", "NMODIF", "NOCOLOR",
               "NODES", "/NOERASE", "/NOLIST", "NOOFFSET", "NOORDER",
               "/NOPR", "NORA", "NORL", "/NORMAL", "NPLOT", "NPRINT",
               "NREAD", "NREFINE", "NRLSUM", "*NRM", "NROPT",
               "NROTAT", "NRRANG", "NSCALE", "NSEL", "NSLA", "NSLE",
               "NSLK", "NSLL", "NSLV", "NSMOOTH", "NSOL", "NSORT",
               "NSTORE", "NSUBST", "NSVR", "NSYM", "/NUMBER",
               "NUMCMP", "NUMEXP", "NUMMRG", "NUMOFF", "NUMSTR",
               "NUMVAR", "NUSORT", "NWPAVE", "NWPLAN", "NWRITE",
               "OCDATA", "OCDELETE", "OCLIST", "OCREAD", "OCTABLE",
               "OCTYPE", "OCZONE", "OMEGA", "OPERATE", "OPNCONTROL",
               "OUTAERO", "OUTOPT", "OUTPR", "/OUTPUT", "OUTRES",
               "OVCHECK", "PADELE", "/PAGE", "PAGET", "PAPUT",
               "PARESU", "PARTSEL", "PARRES", "PARSAV", "PASAVE",
               "PATH", "PAUSE", "/PBC", "/PBF", "PCALC", "PCGOPT",
               "PCIRC", "/PCIRCLE", "/PCOPY", "PCROSS", "PDANL",
               "PDCDF", "PDCFLD", "PDCLR", "PDCMAT", "PDCORR",
               "PDDMCS", "PDDOEL", "PDEF", "PDEXE", "PDHIST",
               "PDINQR", "PDLHS", "PDMETH", "PDOT", "PDPINV",
               "PDPLOT", "PDPROB", "PDRESU", "PDROPT", "/PDS",
               "PDSAVE", "PDSCAT", "PDSENS", "PDSHIS", "PDUSER",
               "PDVAR", "PDWRITE", "PERBC2D", "PERTURB", "PFACT",
               "PHYSICS", "PIVCHECK", "PLCAMP", "PLCFREQ", "PLCHIST",
               "PLCINT", "PLCPLX", "PLCRACK", "PLDISP", "PLESOL",
               "PLETAB", "PLFAR", "PLF2D", "PLGEOM", "PLLS", "PLMAP",
               "PLMC", "PLNEAR", "PLNSOL", "/PLOPTS", "PLORB", "PLOT",
               "PLOTTING", "PLPAGM", "PLPATH", "PLSECT", "PLST",
               "PLTIME", "PLTRAC", "PLVAR", "PLVECT", "PLZZ",
               "/PMACRO", "PMAP", "PMGTRAN", "PMLOPT", "PMLSIZE",
               "/PMORE", "PNGR", "/PNUM", "POINT", "POLY", "/POLYGON",
               "/POST1", "/POST26", "POWERH", "PPATH", "PRANGE",
               "PRAS", "PRCAMP", "PRCINT", "PRCPLX", "PRED",
               "PRENERGY", "/PREP7", "PRERR", "PRESOL", "PRETAB",
               "PRFAR", "PRI2", "PRIM", "PRINT", "*PRINT", "PRISM",
               "PRITER", "PRJSOL", "PRNEAR", "PRNLD", "PRNSOL",
               "PROD", "PRORB", "PRPATH", "PRRFOR", "PRRSOL",
               "PRSCONTROL", "PRSECT", "PRTIME", "PRVAR", "PRVECT",
               "PSCONTROL", "PSCR", "PSDCOM", "PSDFRQ", "PSDGRAPH",
               "PSDRES", "PSDSPL", "PSDUNIT", "PSDVAL", "PSDWAV",
               "/PSEARCH", "PSEL", "/PSF", "PSMAT", "PSMESH",
               "/PSPEC", "/PSTATUS", "PSTRES", "/PSYMB", "PTR",
               "PTXY", "PVECT", "/PWEDGE", "QDVAL", "QRDOPT", "QSOPT",
               "QUAD", "/QUIT", "QUOT", "R", "RACE", "RADOPT",
               "RAPPND", "RATE", "/RATIO", "RBE3", "RCON", "RCYC",
               "RDEC", "RDELE", "READ", "REAL", "REALVAR", "RECTNG",
               "REMESH", "/RENAME", "REORDER", "*REPEAT", "/REPLOT",
               "RESCOMBINE", "RESCONTROL", "RESET", "/RESET", "RESP",
               "RESUME", "RESVEC", "RESWRITE", "*RETURN", "REXPORT",
               "REZONE", "RFORCE", "/RGB", "RIGID", "RIGRESP",
               "RIMPORT", "RLIST", "RMALIST", "RMANL", "RMASTER",
               "RMCAP", "RMCLIST", "/RMDIR", "RMFLVEC", "RMLVSCALE",
               "RMMLIST", "RMMRANGE", "RMMSELECT", "RMNDISP",
               "RMNEVEC", "RMODIF", "RMORE", "RMPORDER", "RMRESUME",
               "RMRGENERATE", "RMROPTIONS", "RMRPLOT", "RMRSTATUS",
               "RMSAVE", "RMSMPLE", "RMUSE", "RMXPORT", "ROCK",
               "ROSE", "RPOLY", "RPR4", "RPRISM", "RPSD", "RSFIT",
               "RSOPT", "RSPLIT", "RSPLOT", "RSPRNT", "RSSIMS",
               "RSTMAC", "RSTOFF", "RSURF", "RSYMM", "RSYS", "RTHICK",
               "SABS", "SADD", "SALLOW", "SAVE", "SBCLIST", "SBCTRAN",
               "SDELETE", "SE", "SECCONTROL", "SECDATA",
               "SECFUNCTION", "SECJOINT", "/SECLIB", "SECLOCK",
               "SECMODIF", "SECNUM", "SECOFFSET", "SECPLOT",
               "SECREAD", "SECSTOP", "SECTYPE", "SECWRITE", "SED",
               "SEDLIST", "SEEXP", "/SEG", "SEGEN", "SELIST", "SELM",
               "SELTOL", "SENERGY", "SEOPT", "SESYMM", "*SET", "SET",
               "SETFGAP", "SETRAN", "SEXP", "SF", "SFA", "SFACT",
               "SFADELE", "SFALIST", "SFBEAM", "SFCALC", "SFCUM",
               "SFDELE", "SFE", "SFEDELE", "SFELIST", "SFFUN",
               "SFGRAD", "SFL", "SFLDELE", "SFLEX", "SFLIST",
               "SFLLIST", "SFSCALE", "SFTRAN", "/SHADE", "SHELL",
               "/SHOW", "/SHOWDISP", "SHPP", "/SHRINK", "SLIST",
               "SLOAD", "SMALL", "*SMAT", "SMAX", "/SMBC", "SMBODY",
               "SMCONS", "SMFOR", "SMIN", "SMOOTH", "SMRTSIZE",
               "SMSURF", "SMULT", "SNOPTION", "SOLU", "/SOLU",
               "SOLUOPT", "SOLVE", "SORT", "SOURCE", "SPACE",
               "SPCNOD", "SPCTEMP", "SPDAMP", "SPEC", "SPFREQ",
               "SPGRAPH", "SPH4", "SPH5", "SPHERE", "SPLINE", "SPLOT",
               "SPMWRITE", "SPOINT", "SPOPT", "SPREAD", "SPTOPT",
               "SPOWER", "SPUNIT", "SPVAL", "SQRT", "*SREAD", "SRSS",
               "SSBT", "/SSCALE", "SSLN", "SSMT", "SSPA", "SSPB",
               "SSPD", "SSPE", "SSPM", "SSUM", "SSTATE", "STABILIZE",
               "STAOPT", "STAT", "*STATUS", "/STATUS", "STEF",
               "/STITLE", "STORE", "SUBOPT", "SUBSET", "SUCALC",
               "SUCR", "SUDEL", "SUEVAL", "SUGET", "SUMAP", "SUMTYPE",
               "SUPL", "SUPR", "SURESU", "SUSAVE", "SUSEL", "SUVECT",
               "SV", "SVPLOT", "SVTYP", "SWADD", "SWDEL", "SWGEN",
               "SWLIST", "SYNCHRO", "/SYP", "/SYS", "TALLOW",
               "TARGET", "*TAXIS", "TB", "TBCOPY", "TBDATA", "TBDELE",
               "TBEO", "TBIN", "TBFIELD", "TBFT", "TBLE", "TBLIST",
               "TBMODIF", "TBPLOT", "TBPT", "TBTEMP", "TCHG", "/TEE",
               "TERM", "THEXPAND", "THOPT", "TIFF", "TIME",
               "TIMERANGE", "TIMINT", "TIMP", "TINTP", "/TITLE",
               "/TLABEL", "TOFFST", "*TOPER", "TORQ2D", "TORQC2D",
               "TORQSUM", "TORUS", "TRANS", "TRANSFER", "*TREAD",
               "TREF", "/TRIAD", "/TRLCY", "TRNOPT", "TRPDEL",
               "TRPLIS", "TRPOIN", "TRTIME", "TSHAP", "/TSPEC",
               "TSRES", "TUNIF", "TVAR", "/TXTRE", "/TYPE", "TYPE",
               "/UCMD", "/UDOC", "/UI", "UIMP", "/UIS", "*ULIB",
               "UNDELETE", "UNDO", "/UNITS", "UNPAUSE", "UPCOORD",
               "UPGEOM", "*USE", "/USER", "USRCAL", "USRDOF",
               "USRELEM", "V", "V2DOPT", "VA", "*VABS", "VADD",
               "VARDEL", "VARNAM", "VATT", "VCLEAR", "*VCOL",
               "/VCONE", "VCROSS", "*VCUM", "VDDAM", "VDELE", "VDGL",
               "VDOT", "VDRAG", "*VEC", "*VEDIT", "VEORIENT", "VEXT",
               "*VFACT", "*VFILL", "VFOPT", "VFQUERY", "VFSM",
               "*VFUN", "VGEN", "*VGET", "VGET", "VGLUE", "/VIEW",
               "VIMP", "VINP", "VINV", "*VITRP", "*VLEN", "VLIST",
               "VLSCALE", "*VMASK", "VMESH", "VOFFST", "VOLUMES")

    # list of in-built () functions
    elafunf = ("NX()", "NY()", "NZ()", "KX()", "KY()", "KZ()", "LX()",
               "LY()", "LZ()", "LSX()", "LSY()", "LSZ()", "NODE()",
               "KP()", "DISTND()", "DISTKP()", "DISTEN()", "ANGLEN()",
               "ANGLEK()", "NNEAR()", "KNEAR()", "ENEARN()",
               "AREAND()", "AREAKP()", "ARNODE()", "NORMNX()",
               "NORMNY()", "NORMNZ()", "NORMKX()", "NORMKY()",
               "NORMKZ()", "ENEXTN()", "NELEM()", "NODEDOF()",
               "ELADJ()", "NDFACE()", "NMFACE()", "ARFACE()", "UX()",
               "UY()", "UZ()", "ROTX()", "ROTY()", "ROTZ()", "TEMP()",
               "PRES()", "VX()", "VY()", "VZ()", "ENKE()", "ENDS()",
               "VOLT()", "MAG()", "AX()", "AY()", "AZ()",
               "VIRTINQR()", "KWGET()", "VALCHR()", "VALHEX()",
               "CHRHEX()", "STRFILL()", "STRCOMP()", "STRPOS()",
               "STRLENG()", "UPCASE()", "LWCASE()", "JOIN()",
               "SPLIT()", "ABS()", "SIGN()", "CXABS()", "EXP()",
               "LOG()", "LOG10()", "SQRT()", "NINT()", "MOD()",
               "RAND()", "GDIS()", "SIN()", "COS()", "TAN()",
               "SINH()", "COSH()", "TANH()", "ASIN()", "ACOS()",
               "ATAN()", "ATAN2()")

    elafung = ("NSEL()", "ESEL()", "KSEL()", "LSEL()", "ASEL()",
               "VSEL()", "NDNEXT()", "ELNEXT()", "KPNEXT()",
               "LSNEXT()", "ARNEXT()", "VLNEXT()", "CENTRX()",
               "CENTRY()", "CENTRZ()")

    elafunh = ("~CAT5IN", "~CATIAIN", "~PARAIN", "~PROEIN", "~SATIN",
               "~UGIN", "A", "AADD", "AATT", "ABEXTRACT", "*ABBR",
               "ABBRES", "ABBSAV", "ABS", "ACCAT", "ACCOPTION",
               "ACEL", "ACLEAR", "ADAMS", "ADAPT", "ADD", "ADDAM",
               "ADELE", "ADGL", "ADRAG", "AESIZE", "AFILLT", "AFLIST",
               "AFSURF", "*AFUN", "AGEN", "AGLUE", "AINA", "AINP",
               "AINV", "AL", "ALIST", "ALLSEL", "ALPHAD", "AMAP",
               "AMESH", "/AN3D", "ANCNTR", "ANCUT", "ANCYC", "ANDATA",
               "ANDSCL", "ANDYNA", "/ANFILE", "ANFLOW", "/ANGLE",
               "ANHARM", "ANIM", "ANISOS", "ANMODE", "ANMRES",
               "/ANNOT", "ANORM", "ANPRES", "ANSOL", "ANSTOAQWA",
               "ANSTOASAS", "ANTIME", "ANTYPE")

    tokens = {
        'root': [
            (r'!.*\n', Comment),
            include('strings'),
            include('core'),
            include('nums'),
            (words((elafunb+elafunc+elafund+elafune+elafunh), suffix=r'\b'), Keyword),
            (words((elafunf+elafung), suffix=r'\b'), Name.Builtin),
            (r'AR[0-9]+', Name.Variable.Instance),
            (r'[a-z][a-z0-9_]*', Name.Variable),
            (r'[\s]+', Whitespace),
        ],
        'core': [
            # Operators
            (r'(\*\*|\*|\+|-|\/|<|>|<=|>=|==|\/=|=)', Operator),
            (r'/EOF', Generic.Emph),
            (r'[(),:&;]', Punctuation),
        ],
        'strings': [
            (r'(?s)"(\\\\|\\[0-7]+|\\.|[^"\\])*"', String.Double),
            (r"(?s)'(\\\\|\\[0-7]+|\\.|[^'\\])*'", String.Single),
            (r'[$%]', String.Symbol),
        ],
        'nums': [
            (r'\d+(?![.ef])', Number.Integer),
            (r'[+-]?\d*\.?\d+([ef][-+]?\d+)?', Number.Float),
            (r'[+-]?\d+\.?\d*([ef][-+]?\d+)?', Number.Float),
        ]
    }
