"""
TODO: redo 3507... there are actually 3 figures there... well, maybe, the models are the same

TODO: 146376: need to load morphometric file... not sure what it wants... need to manually curate
TODO: 139656 -- large network
TODO: 97917
TODO: 93326 -- maybe this should be more than 1... depending on VClamp/IClamp?

Some models need manual intervention:
53869 -- press enter after the h.restart

136715 -- contains additional instructions in the readme about changing parameters, which these instructions do not do

Skipped 39948 -- lots of buttons, not immediately clear how to use

Skipped for now: Traub et al 2005
123897_2 crashes with "NEURON: procedure too big", also have to rename lib/U_Dvdt.hoc to fix case sensitive filename issue
93321_* causes classic modelview to core dump
143635 -- Amanda Casale's model only presents one parameter set when run with mosinit.hoc, but two others are available; should these be viewable in modelview?
28316_1 -- classic modelview crashes due to point processes not being inserted in a section... still need to put in the rest of 28316_*, but seems no point for now

127388 -- interesting model. no fadvance

144586 -- no sections. no modelview yet

71312 -- skipped for now, not sure if 1 modelview or 16

20212 -- to run, need to have . on path
"""

"""
added today:

143719, 9769_*, 148094, 116983, 112546_*, 19696_*, 126776_*, 138205, 55035, 144490, 87535, 144976_*, 144392_*, 118986, 136176, 3263_*, 35358, 20007, 101629_*, 3332, 37857_*, 37856_*, 3509_*, 146376, 118098, 140462, 151458, 150551_*, 125745, 112086_*, 3800, 144520, 126467, 112685, 48332, 17664, 80769_*, 147578_*, 93326, 3434, 53435_*

added from bottom up:
64212

Next time: put today's on the server

deal with 20212 (Poirazi?) -- only have one so far
remove 20212_2 since missing a variable definition? or make work?

    '20212_2':
        {
            'variant': 'Disperse Equal Sized',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Disperse_equal_sized.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },        

"""
automatically_curated_protocols = {
    '93326':
        {
            'compile': ['cd ngetting', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ngetting']
        },
    '3434':
        {
            'compile': ['cd cdlab', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr cdlab']
        },
    '64212':
        {
            'compile': ['cd VNO', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VNO']
        },
    '147578_1':
        {
            'variant': 'Compute Input Resistances Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("RN_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '147578_2':
        {
            'variant': 'Save Local Chirp Responses for Locations Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Chirp_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '80769_1':
        {
            'variant': 'Off On Off original protocol',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("restart(\\"OFF_ON_OFF_protocol\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '80769_2':
        {
            'variant': 'Short demo run simulation',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("restart(\\"shortRun\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '17664':
        {
            'compile': ['cd prknj', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr prknj']
        },
    '48332':
        {
            'compile': ['cd purkinje', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr purkinje']
        },
    '112685':
        {
            'compile': ['cd Golgi_cell', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Golgi_cell']
        },
    '126467':
        {
            'compile': ['cd NegroniLascano', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr NegroniLascano']
        },
    '144520':
        {
            'compile': ['cd DiFrancescoNoble1985', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr DiFrancescoNoble1985']
        },
    '3800':
        {
            'compile': ['cd cardiac1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr cardiac1998']
        },
    '125745':
        {
            'compile': ['cd fink2000', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr fink2000']
        },
    '150551_1':
        {
            'variant': 'Figure 4F-G',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig4F-G.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '150551_2':
        {
            'variant': 'Figure 6C-F',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig6C-F.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '108458':
        {
            'compile': ['cd KampaStuart2006', 'nrnivmodl mod'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr KampaStuart2006']
        },
    '151458':
        {
            'compile': ['cd Nakano_FICN_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr Nakano_FICN_model']
        },
    '140462':
        {
            'compile': ['cd MasurkarChen2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig7c()'],
            'cleanup': ['cd ../', 'rm -fr MasurkarChen2011']
        },
    '118098':
        {
            'compile': ['cd ca3-summ', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3-summ']
        },
    '76879_1':
        {
            'variant': 'No drive (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(1)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_2':
        {
            'variant': 'Driven (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(2)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_3':
        {
            'variant': 'As set (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(3)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_4':
        {
            'variant': 'No drive (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(4)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_5':
        {
            'variant': 'Driven (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(5)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_6':
        {
            'variant': 'As set (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run1(6)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '3509_1':
        {
            'variant': 'rate',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("prate()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_2':
        {
            'variant': 'steady state current',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("pcur2()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_3':
        {
            'variant': 'voltage clamp',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("pvc()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3332':
        {
            'compile': ['cd h_cno', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr h_cno']
        },
    '101629_1':
        {
            'variant': 'Fig.9B',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("fig9b()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_2':
        {
            'variant': 'Fig.9C',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("fig9c()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_3':
        {
            'variant': 'Fig.9D',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("fig9d()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_4':
        {
            'variant': 'Fig.9E',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("fig9e()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '126814':
        {
            'compile': ['cd develop', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr develop']
        },
    '20007':
        {
            'compile': ['cd ca3_2002', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ca3_2002']
        },
    '3263_1':
        {
            'variant': 'burst',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runb()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_2':
        {
            'variant': 'no-burst short',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runnbs()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_3':
        {
            'variant': 'no-burst long',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runnbl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '118986':
        {
            'compile': ['cd mutant', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr mutant']
        },
    '144392_1':
        {
            'variant': 'soma=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runs()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_2':
        {
            'variant': 'km in both',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_3':
        {
            'variant': 'axon=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144976_1':
        {
            'variant': 'control',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("control()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_2':
        {
            'variant': 'alzheimer',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("AD()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_3':
        {
            'variant': 'KA-treatment',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("AD_KA()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '87535':
        {
            'compile': ['cd magical7', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr magical7']
        },
    '55035':
        {
            'compile': ['cd obliques', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr obliques']
        },
    '126776_1':
        {
            'variant': 'control',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runc()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_2':
        {
            'variant': '4-AP',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run4ap()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_3':
        {
            'variant': '4-AP+ZD',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run4apzd()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '19696_1':
        {
            'variant': 'full model (black)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runf()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_2':
        {
            'variant': 'uniform KA (red)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_3':
        {
            'variant': 'uniform KA and I-h (blue)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runh()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '112546_1':
        {
            'variant': 'fig.4(i)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runi()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_2':
        {
            'variant': 'fig.4(ii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_3':
        {
            'variant': 'fig.4(iii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runiii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_4':
        {
            'variant': 'fig.4(iv)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '116983':
        {
            'compile': ['cd theta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr theta']
        },
    '148094':
        {
            'compile': ['cd kv72-R213QW-mutations', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr kv72-R213QW-mutations']
        },
    '9769_distal':
        {
            'variant': 'distal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("rund()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        },
    '9769_proximal':
        {
            'variant': 'proximal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runp()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        }

}

manually_curated_protocols = {
    '53435_1':
        {
            'variant': 'Real EPSP',
            'compile': ['cd anyas2005/model_bf_real_EPSP', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '53435_2':
        {
            'variant': 'HPP',
            'compile': ['cd anyas2005/model_bf_HPP', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '112086_1':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("metal()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_2':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("cntel()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_3':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("cntel2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },

    '37856_1':
        {
            'variant': 'Fig 2',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_2':
        {
            'variant': 'Fig 3A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_3':
        {
            'variant': 'Fig 3B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_4':
        {
            'variant': 'Fig 4A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_5':
        {
            'variant': 'Fig 4B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_6':
        {
            'variant': 'Fig 10A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_7':
        {
            'variant': 'Fig 10B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37857_1':
        {
            'variant': 'Figure2A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig2A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_2':
        {
            'variant': 'Figure2B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig2B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_3':
        {
            'variant': 'Figure2C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig2C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_4':
        {
            'variant': 'Figure2D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig2D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_5':
        {
            'variant': 'Panel A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig3A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_6':
        {
            'variant': 'Panel B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig3B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_7':
        {
            'variant': 'Panel C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig3C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_8':
        {
            'variant': 'Panel D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig3D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_9':
        {
            'variant': 'Type I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig4A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_10':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig4B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_11':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig4C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_12':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Fig4D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_13':
        {
            'variant': 'Type I-c',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type1c()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_14':
        {
            'variant': 'Type I-t',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type1t()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_15':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type12()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_16':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type21()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_17':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_18':
        {
            'variant': 'Type IIo (Octopus)',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("Type2o()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '35358':
        {
            'compile': ['cd b04feb12', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr b04feb12']
        },
    '136176':
        {
            'compile': ['cd Katona_et_al', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Katona_et_al']
        },
    '138205':
        {
            'compile': ['cd Schizophr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h("display_cell()")'],
            'cleanup': ['cd ../', 'rm -fr Schizophr']
        },
    '144490':
        {
            'compile': ['cd bpap', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.gui_run_bpap()'],
            'cleanup': ['cd ../', 'rm -fr bpap']
        },
    '143719':
        {
            'compile': ['cd Ca1_Bianchi/experiment', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr Ca1_Bianchi']
        },

    '20212_1':
        {
            'variant': 'Disperse 6_2',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Disperse_6_2.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },
    '44050_1':
        {
            'variant': 'Control',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_2':
        {
            'variant': 'AMPA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runa()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_3':
        {
            'variant': 'AMPA + NMDA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '144541_1':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("fig-5a.hoc")', 'h.loop()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },        
    '144541_2':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("fig-5a.hoc")', 'h.zd()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr SousaEtAl2014']
        },
    '7509':
        {
            'compile': ['cd magee2000'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr magee2000'],
            'stopmidsim': False       # need this because an xpanel is open until after the sim completes
        },
    '106551':
        {
            'compile': ['cd nc-mri', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr nc-mri']
        },
    '3507':
        {
            'compile': ['cd fh', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fh']
        },
    '7386':
        {
            'compile': ['cd boosting', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr boosting']
        },
    '125152':
        {
            'compile': ['cd Uebachs-et-al_2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr Uebachs-et-al_2010']
        },
    '2796_1':
        {
            'variant': 'Fig 1A',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("fig_1a.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '2796_2':
        {
            'variant': 'Fig 1C',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("fig_1c.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '144401':
        {
            'compile': ['cd VladimirovTuTraub2012', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr VladimirovTuTraub2012']
        },
    '87546':
        {
            'compile': ['cd olm-int', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr olm-int']
        },
    '20015':
        {
            'compile': ['cd k_interneurons', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("kinetics.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr k_interneurons']
        },
    '32992':
        {
            'compile': ['cd synchro-ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr synchro-ca1']
        },
    '2937_1':
        {
            'variant': 'Fig 3',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run3()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_2':
        {
            'variant': 'Fig 4bc',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run4bc()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_3':
        {
            'variant': 'Fig 4bd',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run4bd()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '139418_1':
        {
            'variant': 'Fig 11',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("figure11.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '139418_2':
        {
            'variant': 'Fig 13',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("figure13.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '46839':
        {
            'compile': ['cd GranuleCell', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr GranuleCell']
        },
    '116830':
        {
            'compile': ['cd b08dec23', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("init.hoc")'],
            'cleanup': ['cd ..', 'rm -fr b08dec23']
        },
    '125689':
        {
            'compile': ['cd CarvalhoBuonomano/Neuron2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.MULTI()'],
            'cleanup': ['cd ../..', 'rm -fr CarvalhoBuonomano']
        },
    '127388':
        {
            'compile': ['cd BGnet', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run_sim()'],
            'cleanup': ['cd ../..', 'rm -fr BGnet']
        },
    '136803':
        {
            'compile': ['cd JonesEtAl2009', 'nrnivmodl mod_files'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr JonesEtAl2009']
        },
    '116096_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -100', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -10', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.35)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_3':
        {
            'variant': 'Fig 2C',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 10', 'h.set_axis_limits(0.0045, 0.5, 0.9, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '116096_4':
        {
            'variant': 'Fig 2D',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 200', 'h.ampasyn.onset = 10', 'h.set_axis_limits(0.0016, 0.016, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '147538_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.Fig2A()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '147538_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.Fig2B()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '112834':
        {
            'compile': ['cd nacb_msp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr nacb_msp']
        },
    '125378':
        {
            'compile': ['cd leeEtAl2003', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig8b()'],
            'cleanup': ['cd ..', 'rm -fr leeEtAl2003']
        },
    '115356':
        {
            'compile': ['cd RoyeckEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr RoyeckEtAl2008']
        },
    '127021':
        {
            'compile': ['cd Golgi_cell_NaKATPAse', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.recreate()'],
            'cleanup': ['cd ..', 'rm -fr Golgi_cell_NaKATPAse']
        },
    '147514':
        {
            'compile': ['cd dendritic_complexity', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr dendritic_complexity']
        },
    '135838':
        {
            'compile': ['cd Alle_et_al_2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Alle_et_al_2009']
        },
    '143635':
        {
            'compile': ['cd CasaleEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.measure()'],
            'cleanup': ['cd ..', 'rm -fr CasaleEtAl2011']
        },
    '87473':
        {
            'compile': ['cd weaver_SimAnn_ObjFcn', 'nrnivmodl model optmz'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr weaver_SimAnn_ObjFcn']
        },
    '135839':
        {
            'compile': ['cd McCormickEtAl2007YuEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
            'cleanup': ['cd ..', 'rm -fr McCormickEtAl2007YuEtAl2008']
        },
    '127992':
        {
            'compile': ['cd HHcn', 'nrnivmodl mod-files/', 'cp python/* .'],
            'launch': ['nrngui -python'],
            'run': ['execfile("HHneuron.py")'],
            'cleanup': ['cd ..', 'rm -fr HHcn']
        },
    '145836':
        {
            'compile': ['cd MoradiEtAl2012', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MoradiEtAl2012']
        },
    '28316_1':
        {
            'variant': '8A Long',
            'compile': ['cd OLMmodel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("initFig8Along")'],
            'cleanup': ['cd ..', 'rm -fr OLMmodel']
        },
    '3785_1':
        {
            'variant': 'Figure 3 1A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h.fig1A_vitro()'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_2':
        {
            'variant': 'Figure 4 2A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("mcab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_3':
        {
            'variant': "Figure 4 2A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("ecab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_4':
        {
            'variant': "Figure 5 3A in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("mcab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_5':
        {
            'variant': "Figure 5 3A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("ecab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '87284_1':
        {
            'variant': 'Figure 1, 2',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig1and2()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_2':
        {
            'variant': 'Figure 3',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_3':
        {
            'variant': 'Figure 4',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig4()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_4':
        {
            'variant': 'Figure 5',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig5()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_5':
        {
            'variant': 'Figure 6',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '18198_1':
        {
            'variant': 'Synaptic Release',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("release")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_2':
        {
            'variant': 'AMPA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("ampa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_3':
        {
            'variant': 'AMPA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("ampa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_4':
        {
            'variant': 'NMDA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("nmda")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_5':
        {
            'variant': 'NMDA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("nmda5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_6':
        {
            'variant': 'GABA_A - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_7':
        {
            'variant': 'GABA_A - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_8':
        {
            'variant': 'GABA_B - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("gabab")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_9':
        {
            'variant': 'GABA_B - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("gabab3")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '136715_1':
        {
            'variant': 'Fig 6B',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig6B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_2':
        {
            'variant': 'Fig 4B 10APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 10APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_3':
        {
            'variant': 'Fig 4B 100APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 100APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_4':
        {
            'variant': 'Fig 3A',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig3A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '93321_1':
        {
            'variant': 'Fig 3A (top left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3topleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_2':
        {
            'variant': 'Fig 3B (top right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3topright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_3':
        {
            'variant': 'Fig 3A middle (left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3middleleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_4':
        {
            'variant': 'Fig 3B middle (right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'stopmidsim': False,
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3middleright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_5':
        {
            'variant': 'Fig 3 bottom',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.fig3bottom()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '123897_1':
        {
            'variant': 'Pyramidal Cell',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/Pyramidal_Main.hoc")', 'h.freePlay()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_2':
        {
            'variant': 'Uniform Axon',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/UniformAxon_Main.hoc")'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_3':
        {
            'variant': 'Single Compartment (activation)',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/SingleComp_Main.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '19176_1':
        {
            'variant': 'Current Steps',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.experiment1()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '19176_2':
        {
            'variant': 'cAMP pulse',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.experiment2()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '124063':
        {
            'compile': ['cd PublioEtAl2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.start()'],
            'cleanup': ['cd ..', 'rm -fr PublioEtAl2009']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_2':
        {
            'variant': 'Fig 7C: hh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-hh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_3':
        {
            'variant': 'Fig 7C: NaCh-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-NaCh-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_4':
        {
            'variant': 'Fig 7C: NaCh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-NaCh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_5':
        {
            'variant': 'Fig 7C: NaCh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-NaCh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_6':
        {
            'variant': 'Fig 7C: naf-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naf-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_7':
        {
            'variant': 'Fig 7C: naf-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naf-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_8':
        {
            'variant': 'Fig 7C: naf-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naf-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_9':
        {
            'variant': 'Fig 7C: naxn-black',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naxn-black.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_10':
        {
            'variant': 'Fig 7C: naxn-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naxn-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_11':
        {
            'variant': 'Fig 7C: naxn-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7C-naxn-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_12':
        {
            'variant': 'Fig 7D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_13':
        {
            'variant': 'Fig 7E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7E.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_14':
        {
            'variant': 'Fig 6B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_15':
        {
            'variant': 'Fig 6C',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-C.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_16':
        {
            'variant': 'Fig 7B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_17':
        {
            'variant': 'Fig 6D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_18':
        {
            'variant': 'Fig 6E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_19':
        {
            'variant': 'Fig 6F',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-F.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_20':
        {
            'variant': 'Fig 7A',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig7A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_21':
        {
            'variant': 'Fig 6B-inset',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("Fig6-B-inset.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '126637_2c':
        {
            'variant': 'Fig 2C + 2E',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_spine and spine neck at spinydendrite133.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_2d':
        {
            'variant': 'Fig 2D + 2F',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_reduced_PPR model.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_cvode':
        {
            'variant': 'CVODE or other solvers',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_reduced_PPR model_cvode.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '146026_ex1':
        {
            'variant': 'Example 1',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example1.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex2':
        {
            'variant': 'Example 2',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example2.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex3':
        {
            'variant': 'Example 3',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example3.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '137259':
        {
            'compile': ['cd ca3-synresp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr ca3-synresp']
        },
    '53869':
        {
            'compile': ['cd MSO_Zhouetal_2005', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("MSO_Zhouetal_2005")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MSO_Zhouetal_2005']
        },
    '125857_2frb':
        {
            'variant': '2FRB',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("2FRB")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '140249_a1':
        {
            'variant': 'Fig 4 A1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP1MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b1':
        {
            'variant': 'Fig 4 B1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP1HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_a2':
        {
            'variant': 'Fig 4 A2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP2MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b2':
        {
            'variant': 'Fig 4 B2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP2HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },        
    '125857_frb3':
        {
            'variant': 'FRB3',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB3")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_19':
        {
            'variant': 'FRB_12_19',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_19")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_21':
        {
            'variant': 'FRB_12_21',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_21")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '150240':
        {
            'compile': ['cd TCconvergenceModel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr TCconvergenceModel']
        }
}

protocol = dict(automatically_curated_protocols)
protocol.update(manually_curated_protocols)

if __name__ == '__main__':
    import json
    multi = {}
    for key in protocol:
        split = key.split('_')
        if len(split) > 1:
            if split[0] not in multi:
                multi[split[0]] = []
            multi[split[0]].append([protocol[key]['variant'], key])
    for id in multi:
        multi[id] = sorted(multi[id], key=lambda row: row[0])
    print json.dumps(multi)
