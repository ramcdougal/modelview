"""
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

144541_*, 7509, 106551, 7386, 44050_*, 151949, 3507

Next time:

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
protocol = {
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
