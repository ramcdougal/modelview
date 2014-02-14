"""
TODO: redo 3507... there are actually 3 figures there... well, maybe, the models are the same

TODO: 146376: need to load morphometric file... not sure what it wants... need to manually curate
TODO: 139656 -- large network
TODO: 97917_*
TODO: 93326 -- maybe this should be more than 1... depending on VClamp/IClamp?
TODO: 147366 -- this is a lytton model... nonstandard setup
TODO: 140881 -- another lytton model... no fadvances, json_generator fails
TODO: 12631 -- another lytton model... no fadvances, json_generator fails
TODO: 19366_1 -- doesn't actually run... need to click the "Plot" buttons, but not clear where they come from
TODO: 22203 -- runs everything in a different process!
TODO: 124513 -- large model, complains about not running an fadvance, but seems like it must
TODO: 95960 -- can switch between many cells and many figures...
TODO: 51781 -- large network
TODO: 84612 -- push buttons... many many push buttons
TODO: 147460 -- buried code, no mosinit... shouldn't be that hard, looks like only two cases
TODO: 53437 -- possibly no sections?
TODO: 140038 -- push buttons, needs a manual setup
TODO: 144511 -- python... no mosinit.hoc (shouldn't be hard, but needs a manual setup)
TODO: 138379 -- no sections (lytton model)
TODO: 117207_* -- button pressing troubles (e.g. 'hoc.HocObject' object has no attribute 'RunBestFit')
TODO: 76879_* -- no sections (ermentrout)
TODO: 151404 -- runs with a script instead of mosinit... need to figure out what to do herer
TODO: 84589 -- no mosinit.hoc, but seems like it should have one (emailed Tom)
TODO: confirm 52034 sets up a structure (it says it doesn't run... figure out why not)
TODO: 21984 -- no sections
TODO: 140299_* -- should also have mixed diameter buttons but the files were missing when the run protocols were generated
TODO: 98017 -- useless mosinit, readme... no way of knowing how to run, lots of hoc files
TODO: 97985 -- shell scripts
TODO: 113435 -- modelview available, but only for 113435 which is an alternate of the xpp model 97747... database issues
TODO: 3658: lots of options, needs manual setup
TODO: 135902 -- can't figure out how to run
TODO: 114355 -- needs manual setup; many cell choices (see runme: main file is main.hoc)
TODO: 144549 -- no sections

Some models need manual intervention:
53869 -- press enter after the h.restart
143114_* -- press enter after h.load_file

136715 -- contains additional instructions in the readme about changing parameters, which these instructions do not do

Skipped 39948 -- lots of buttons, not immediately clear how to use

Skipped for now: Traub et al 2005
123897_2 crashes with "NEURON: procedure too big", also have to rename lib/U_Dvdt.hoc to fix case sensitive filename issue
93321_* causes classic modelview to core dump
143635 -- Amanda Casale's model only presents one parameter set when run with mosinit.hoc, but two others are available; should these be viewable in modelview?
28316_1 -- classic modelview crashes due to point processes not being inserted in a section... still need to put in the rest of 28316_*, but seems no point for now
141273 -- no mosinit.hoc; not clear what's going on

127388 -- interesting model. no fadvance

144586 -- no sections. no modelview yet

71312 -- skipped for now, not sure if 1 modelview or 16

20212 -- to run, need to have . on path
"""

"""
added today:

114735, 114047, 7400, 144376_*, 113997_*, 123623_*, 2798_*

added from bottom up:


***
NEXT TIME
***

From top down: Ih levels roles in bursting and regular-spiking subiculum pyramidal neurons (van Welie et al 2006)
From bottom up: Voltage-based STDP synapse (Clopath et al. 2010)




deal with 20212 (Poirazi?) -- only have one so far
remove 20212_2 since missing a variable definition? or make work?

    '20212_2':
        {
            'variant': 'Disperse Equal Sized',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Disperse_equal_sized.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },        

"""
automatically_curated_protocols = {
    '2798_1':
        {
            'variant': 'before training',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_u()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '2798_2':
        {
            'variant': 'after training',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_c()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '2798_3':
        {
            'variant': 'random activation',
            'compile': ['cd HB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_r()'],
            'cleanup': ['cd ../', 'rm -fr HB']
        },
    '114735':
        {
            'compile': ['cd HFO', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HFO']
        },
    '115357_1':
        {
            'variant': '++',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeplusplus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_2':
        {
            'variant': '+-',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeplusminus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_3':
        {
            'variant': '-+',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeminusplus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '115357_4':
        {
            'variant': '--',
            'compile': ['cd GeneralizedCarnevaleHinesScheme', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.makeminusminus()'],
            'cleanup': ['cd ../', 'rm -fr GeneralizedCarnevaleHinesScheme']
        },
    '26997_1':
        {
            'variant': 'Fig 1A',
            'compile': ['cd wang1996', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1a()'],
            'cleanup': ['cd ../', 'rm -fr wang1996']
        },
    '26997_2':
        {
            'variant': 'Fig 3A',
            'compile': ['cd wang1996', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3a()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr wang1996']
        },
    '21329':
        {
            'compile': ['cd inhibnet', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr inhibnet']
        },
    '114685_1':
        {
            'variant': 'Short test run of the GPi neuron similar to Fig 1A',
            'compile': ['cd JohnsonMcIntyre2008', 'nrnivmodl GPi_model'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.short_run()'],
            'cleanup': ['cd ../', 'rm -fr JohnsonMcIntyre2008']
        },
    '114685_2':
        {
            'variant': 'Sample run for the current injections that created Fig 2C',
            'compile': ['cd JohnsonMcIntyre2008', 'nrnivmodl GPi_model'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig2c_point()'],
            'cleanup': ['cd ../', 'rm -fr JohnsonMcIntyre2008']
        },
    '146509':
        {
            'compile': ['cd Branch_Point_Tapering', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_simulation()'],
            'cleanup': ['cd ../', 'rm -fr Branch_Point_Tapering']
        },
    '139654_1':
        {
            'variant': 'Phasic model T8 step',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 1")', 'h("amp = 1")', 'h("cell_type = 1")', 'h("cell_nr = 8")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_2':
        {
            'variant': 'Phasic model T8 ZAP',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 2")', 'h("amp = 1")', 'h("cell_type = 1")', 'h("cell_nr = 8")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_3':
        {
            'variant': 'Tonic model T1 step',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 1")', 'h("amp = 0.6")', 'h("cell_type = 2")', 'h("cell_nr = 1")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_4':
        {
            'variant': 'Tonic model T1 ZAP',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("stim_type = 2")', 'h("amp = 0.5")', 'h("cell_type = 2")', 'h("cell_nr = 1")',  'h.restart()', 'h.load_file(1, "control.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_5':
        {
            'variant': 'Synaptic train stimulation, with inhibition',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("ton_inhib = 1")', 'h("cell_nr = 7")',  'h.restart()', 'h.load_file(1, "traincontrol.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '139654_6':
        {
            'variant': 'Synaptic train stimulation, no inhibition',
            'compile': ['cd 2VN', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("ton_inhib = 0")', 'h("cell_nr = 7")',  'h.restart()', 'h.load_file(1, "traincontrol.hoc")'],
            'cleanup': ['cd ../', 'rm -fr 2VN']
        },
    '140299_1':
        {
            'variant': 'BE17BNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE17B_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_2':
        {
            'variant': 'BE59DNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE59D_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_3':
        {
            'variant': 'BE77CNoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("BE77C_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '140299_4':
        {
            'variant': 'LV38ENoActive',
            'compile': ['cd KubotaEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.loadModel("LV38E_length_adjusted_NoActive.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr KubotaEtAl2011']
        },
    '116956':
        {
            'compile': ['cd vs4_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig10e()'],
            'cleanup': ['cd ../', 'rm -fr vs4_modelDB']
        },
    '8115':
        {
            'compile': ['cd fluct', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr fluct']
        },
    '113435':
        {
            'compile': ['cd fs_internrn_neuron', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr fs_internrn_neuron']
        },
    '8284_1':
        {
            'variant': 'HT',
            'compile': ['cd ihmodel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.HT()'],
            'cleanup': ['cd ../', 'rm -fr ihmodel']
        },
    '8284_2':
        {
            'variant': 'Control',
            'compile': ['cd ihmodel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Control()'],
            'cleanup': ['cd ../', 'rm -fr ihmodel']
        },
    '19022':
        {
            'compile': ['cd geigerEtAl1997', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("fig8d.hoc")'],
            'cleanup': ['cd ../', 'rm -fr geigerEtAl1997']
        },
    '3167':
        {
            'compile': ['cd timing', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runu()'],
            'cleanup': ['cd ../', 'rm -fr timing']
        },
    '3676_1':
        {
            'variant': 'Fig 2',
            'compile': ['cd ephaptic', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig2.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ephaptic']
        },
    '3676_2':
        {
            'variant': 'Fig 3B',
            'compile': ['cd ephaptic', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("fig3.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ephaptic']
        },
    '123815':
        {
            'compile': ['cd Hipp_paper_code', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Hipp_paper_code']
        },
    '120910':
        {
            'compile': ['cd ElectricallycoupledRetziusneurons', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ElectricallycoupledRetziusneurons']
        },
    '116981_1':
        {
            'variant': 'Fig. 5--exc central vs. peripheral tree',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_2':
        {
            'variant': 'Fig. 5 inset--brief excitation',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5inset()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_3':
        {
            'variant': 'Fig. 6--effect of location of excitatory input',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_4':
        {
            'variant': 'Fig. 7--effect of activation sequence',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig7()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '116981_5':
        {
            'variant': 'Fig. 8--effect of inh location',
            'compile': ['cd rall1964', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig8()'],
            'cleanup': ['cd ../', 'rm -fr rall1964']
        },
    '151126':
        {
            'compile': ['cd BianchiEtAl2013', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr BianchiEtAl2013']
        },
    '121060':
        {
            'compile': ['cd MSN2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Exec()'],
            'cleanup': ['cd ../', 'rm -fr MSN2009']
        },
    '148253':
        {
            'compile': ['cd Chloride_Model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Chloride_Model']
        },
    '123453':
        {
            'compile': ['cd AkemannEtAl2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_model( prot )")'],
            'cleanup': ['cd ../', 'rm -fr AkemannEtAl2009']
        },
    '64296_1':
        {
            'variant': 'Figure 2A Top Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Atop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_2':
        {
            'variant': 'Figure 2A Middle Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Amiddle()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_3':
        {
            'variant': 'Figure 2A Bottom Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Abottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_4':
        {
            'variant': 'Figure 2B Top Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Btop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_5':
        {
            'variant': 'Figure 2B Second Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bsecond()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_6':
        {
            'variant': 'Figure 2B Third Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bthird()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_7':
        {
            'variant': 'Figure 2B Bottom Trace',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig2Bbottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_8':
        {
            'variant': 'Figure 3A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_9':
        {
            'variant': 'Figure 3B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_10':
        {
            'variant': 'Figure 3C Top',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3Ctop()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_11':
        {
            'variant': 'Figure 3C Bottom',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig3Cbottom()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_12':
        {
            'variant': 'Figure 4A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig4A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_13':
        {
            'variant': 'Figure 5B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig5B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_14':
        {
            'variant': 'Figure 6A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_15':
        {
            'variant': 'Figure 6B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_16':
        {
            'variant': 'Figure 6C',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6C()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_17':
        {
            'variant': 'Figure 6D',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6D()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_18':
        {
            'variant': 'Figure 6E',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig6E()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_19':
        {
            'variant': 'Figure 7A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig7A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_20':
        {
            'variant': 'Figure 7B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig7B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_21':
        {
            'variant': 'Figure 8A',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8A()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_22':
        {
            'variant': 'Figure 8B',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8B()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '64296_23':
        {
            'variant': 'Figure 8C',
            'compile': ['cd mitral', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig8C()")'],
            'cleanup': ['cd ../', 'rm -fr mitral']
        },
    '118662_1':
        {
            'variant': 'Figure 4a cell 1',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell1\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_2':
        {
            'variant': 'Figure 4a cell 2',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell2\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_3':
        {
            'variant': 'Figure 4a cell 3',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4a_cell3\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_4':
        {
            'variant': 'Figure 4b dendrite 1',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite1\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_5':
        {
            'variant': 'Figure 4b dendrite 2',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite2\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '118662_6':
        {
            'variant': 'Figure 4b dendrite 3',
            'compile': ['cd dm1_pn_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart_(\\"figure_4b_dendrite3\\")")'],
            'cleanup': ['cd ../', 'rm -fr dm1_pn_model']
        },
    '51022':
        {
            'compile': ['cd amirdevor03', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr amirdevor03']
        },
    '140789':
        {
            'compile': ['cd DG_BC/Figure_2', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr DG_BC']
        },
    '116740_1':
        {
            'variant': 'T-Ca',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("control()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '116740_2':
        {
            'variant': 'T-Ca and BK',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("bk()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '116740_3':
        {
            'variant': 'T-Ca and SK',
            'compile': ['cd aradi1999', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("sk()")'],
            'cleanup': ['cd ../', 'rm -fr aradi1999']
        },
    '124291':
        {
            'compile': ['cd FFI/MOPP_Fig_1B_left', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../../', 'rm -fr FFI']
        },
    '3801_1':
        {
            'variant': 'All three synaptic terminals are active',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(3)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_2':
        {
            'variant': 'synapse 0 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(0)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_3':
        {
            'variant': 'synapse 1 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(1)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '3801_4':
        {
            'variant': 'synapse 2 only',
            'compile': ['cd dgbc', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("doit(2)")'],
            'cleanup': ['cd ../', 'rm -fr dgbc']
        },
    '144385':
        {
            'compile': ['cd ShepherdBrayton1979', 'nrnivmodl mod'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr ShepherdBrayton1979']
        },
    '18738':
        {
            'compile': ['cd dendgeom', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr dendgeom']
        },
    '147218':
        {
            'compile': ['cd genet_PC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr genet_PC']
        },
    '124394':
        {
            'compile': ['cd nevian', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr nevian']
        },
    '140828':
        {
            'compile': ['cd Branco_2010', 'nrnivmodl mod.files'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Branco_2010']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr SousaEtAl2014']
        },
   '3344':
        {
            'compile': ['cd ka_dg', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr ka_dg']
        },
    '98005':
        {
            'compile': ['cd D2modulation', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr D2modulation']
        },
    '9853':
        {
            'compile': ['cd joyner80', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr joyner80']
        },
    '52034':
        {
            'compile': ['cd ctxnet', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_fig6()")'],
            'cleanup': ['cd ../', 'rm -fr ctxnet']
        },
    '138382_1':
        {
            'variant': 'Detailed Calcium dynamics model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runDM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_2':
        {
            'variant': 'Calcium transients using different buffering models',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaTransients\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_3':
        {
            'variant': 'Calcium spikes using single pool model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesSP\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_4':
        {
            'variant': 'Calcium spikes using double pool model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDP\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_5':
        {
            'variant': 'Calcium spikes using detailed model',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '138382_6':
        {
            'variant': 'Calcium spikes using DCM',
            'compile': ['cd AnwarEtAl2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"runCaSpikesDCM\\")")'],
            'cleanup': ['cd ../', 'rm -fr AnwarEtAl2010']
        },
    '114637':
        {
            'compile': ['cd SSC_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr SSC_model']
        },
    '9851':
        {
            'compile': ['cd moore78', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr moore78']
        },
    '19366_1':
        {
            'variant': 'Fig.1. A-C',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(1)")'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_2':
        {
            'variant': 'Fig.2. A',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(2)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_3':
        {
            'variant': 'Fig.2. B',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(3)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_4':
        {
            'variant': 'Fig.3. A-D',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(4)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '19366_5':
        {
            'variant': 'Fig.3. E-H',
            'compile': ['cd korogod', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Main(5)")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr korogod']
        },
    '119283_1':
        {
            'variant': '(1-4) Gray - Control',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runi()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_2':
        {
            'variant': '(1) Black - Lamotrigine',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_3':
        {
            'variant': '(2) Black - Diazepam',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiii()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_4':
        {
            'variant': '(3) Black - Flindokalner',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '119283_5':
        {
            'variant': '(4) Black - Lamotrigine+Flindokalner',
            'compile': ['cd FerranteEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runv()")'],
            'cleanup': ['cd ../', 'rm -fr FerranteEtAl2008']
        },
    '123927':
        {
            'compile': ['cd Wimmer-et-al2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run_sim_graph_coarse()")'],
            'cleanup': ['cd ../', 'rm -fr Wimmer-et-al2009']
        },
    '143604_1':
        {
            'variant': 'spine inhibiton with bAP (compartmentalized inhibition)',
            'compile': ['cd singleDendrite', 'nrnivmodl mod'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("spineinhib_bAP_demo()")'],
            'cleanup': ['cd ../', 'rm -fr singleDendrite']
        },
    '143604_2':
        {
            'variant': '10x dend inhib with bAP (widespread inhib with smaller change in amplitude)',
            'compile': ['cd singleDendrite', 'nrnivmodl mod'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("dend10x_bAP_demo()")'],
            'cleanup': ['cd ../', 'rm -fr singleDendrite']
        },
    '93326':
        {
            'compile': ['cd ngetting', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr ngetting']
        },
    '3434':
        {
            'compile': ['cd cdlab', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr cdlab']
        },
    '64212':
        {
            'compile': ['cd VNO', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr VNO']
        },
    '147578_1':
        {
            'variant': 'Compute Input Resistances Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("RN_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '147578_2':
        {
            'variant': 'Save Local Chirp Responses for Locations Along Trunk',
            'compile': ['cd MultiChirp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Chirp_Trunk()")'],
            'cleanup': ['cd ../', 'rm -fr MultiChirp']
        },
    '80769_1':
        {
            'variant': 'Off On Off original protocol',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"OFF_ON_OFF_protocol\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '80769_2':
        {
            'variant': 'Short demo run simulation',
            'compile': ['cd AkemannKnopfelPurkinje_cell_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("restart(\\"shortRun\\")")'],
            'cleanup': ['cd ../', 'rm -fr AkemannKnopfelPurkinje_cell_model']
        },
    '17664':
        {
            'compile': ['cd prknj', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr prknj']
        },
    '48332':
        {
            'compile': ['cd purkinje', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr purkinje']
        },
    '112685':
        {
            'compile': ['cd Golgi_cell', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Golgi_cell']
        },
    '126467':
        {
            'compile': ['cd NegroniLascano', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr NegroniLascano']
        },
    '144520':
        {
            'compile': ['cd DiFrancescoNoble1985', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr DiFrancescoNoble1985']
        },
    '3800':
        {
            'compile': ['cd cardiac1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr cardiac1998']
        },
    '125745':
        {
            'compile': ['cd fink2000', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr fink2000']
        },
    '150551_1':
        {
            'variant': 'Figure 4F-G',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig4F-G.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '150551_2':
        {
            'variant': 'Figure 6C-F',
            'compile': ['cd AshhadNarayanan2013', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("{ load_file(\\"Fig6C-F.hoc\\") }")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr AshhadNarayanan2013']
        },
    '108458':
        {
            'compile': ['cd KampaStuart2006', 'nrnivmodl mod'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr KampaStuart2006']
        },
    '151458':
        {
            'compile': ['cd Nakano_FICN_model', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr Nakano_FICN_model']
        },
    '140462':
        {
            'compile': ['cd MasurkarChen2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig7c()'],
            'cleanup': ['cd ../', 'rm -fr MasurkarChen2011']
        },
    '118098':
        {
            'compile': ['cd ca3-summ', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3-summ']
        },
    '76879_1':
        {
            'variant': 'No drive (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(1)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_2':
        {
            'variant': 'Driven (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(2)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_3':
        {
            'variant': 'As set (slow)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(3)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_4':
        {
            'variant': 'No drive (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(4)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_5':
        {
            'variant': 'Driven (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(5)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '76879_6':
        {
            'variant': 'As set (fast)',
            'compile': ['cd WC', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run1(6)")'],
            'cleanup': ['cd ../', 'rm -fr WC']
        },
    '3509_1':
        {
            'variant': 'rate',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("prate()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_2':
        {
            'variant': 'steady state current',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("pcur2()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3509_3':
        {
            'variant': 'voltage clamp',
            'compile': ['cd kca', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("pvc()")'],
            'cleanup': ['cd ../', 'rm -fr kca']
        },
    '3332':
        {
            'compile': ['cd h_cno', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr h_cno']
        },
    '101629_1':
        {
            'variant': 'Fig.9B',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9b()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_2':
        {
            'variant': 'Fig.9C',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9c()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_3':
        {
            'variant': 'Fig.9D',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9d()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '101629_4':
        {
            'variant': 'Fig.9E',
            'compile': ['cd ca3b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("fig9e()")'],
            'cleanup': ['cd ../', 'rm -fr ca3b']
        },
    '126814':
        {
            'compile': ['cd develop', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr develop']
        },
    '20007':
        {
            'compile': ['cd ca3_2002', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr ca3_2002']
        },
    '3263_1':
        {
            'variant': 'burst',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runb()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_2':
        {
            'variant': 'no-burst short',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runnbs()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '3263_3':
        {
            'variant': 'no-burst long',
            'compile': ['cd ca3_db', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runnbl()")'],
            'cleanup': ['cd ../', 'rm -fr ca3_db']
        },
    '118986':
        {
            'compile': ['cd mutant', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr mutant']
        },
    '144392_1':
        {
            'variant': 'soma=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runs()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_2':
        {
            'variant': 'km in both',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144392_3':
        {
            'variant': 'axon=0',
            'compile': ['cd modeldb', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr modeldb']
        },
    '144976_1':
        {
            'variant': 'control',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("control()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_2':
        {
            'variant': 'alzheimer',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("AD()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '144976_3':
        {
            'variant': 'KA-treatment',
            'compile': ['cd alzheimer', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("AD_KA()")'],
            'cleanup': ['cd ../', 'rm -fr alzheimer']
        },
    '87535':
        {
            'compile': ['cd magical7', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ../', 'rm -fr magical7']
        },
    '55035':
        {
            'compile': ['cd obliques', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr obliques']
        },
    '126776_1':
        {
            'variant': 'control',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runc()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_2':
        {
            'variant': '4-AP',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run4ap()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '126776_3':
        {
            'variant': '4-AP+ZD',
            'compile': ['cd rebound', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run4apzd()")'],
            'cleanup': ['cd ../', 'rm -fr rebound']
        },
    '19696_1':
        {
            'variant': 'full model (black)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runf()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_2':
        {
            'variant': 'uniform KA (red)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runa()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '19696_3':
        {
            'variant': 'uniform KA and I-h (blue)',
            'compile': ['cd sc-pp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runh()")'],
            'cleanup': ['cd ../', 'rm -fr sc-pp']
        },
    '112546_1':
        {
            'variant': 'fig.4(i)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runi()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_2':
        {
            'variant': 'fig.4(ii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_3':
        {
            'variant': 'fig.4(iii)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiii()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '112546_4':
        {
            'variant': 'fig.4(iv)',
            'compile': ['cd km', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr km']
        },
    '116983':
        {
            'compile': ['cd theta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runm()")'],
            'cleanup': ['cd ../', 'rm -fr theta']
        },
    '148094':
        {
            'compile': ['cd kv72-R213QW-mutations', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("run()")'],
            'cleanup': ['cd ../', 'rm -fr kv72-R213QW-mutations']
        },
    '9769_distal':
        {
            'variant': 'distal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("rund()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        },
    '9769_proximal':
        {
            'variant': 'proximal',
            'compile': ['cd lamotrigine', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runp()")'],
            'cleanup': ['cd ../', 'rm -fr lamotrigine']
        }

}

manually_curated_protocols = {
    '123623_1':
        {
            'variant': 'Regular-spiking pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_2':
        {
            'variant': 'Bursting pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_IB")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_3':
        {
            'variant': 'Repetitive bursting pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_IBR")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_4':
        {
            'variant': 'LTS pyramidal cell',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_PY_LTS")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '123623_5':
        {
            'variant': 'Fast-spiking interneuron',
            'compile': ['cd PospischilEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_IN_FS")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr PospischilEtAl2008']
        },
    '7400':
        {
            'compile': ['cd lytton99', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr lytton99']
        },
    '114047':
        {
            'compile': ['cd Basketcell', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.tstop=1e4', 'h.xopen("fig6.hoc")'],
            'cleanup': ['cd ../', 'rm -fr Basketcell']
        },
    '19214_1':
        {
            'variant': 'Fig.1. A,C',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(1)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_2':
        {
            'variant': 'Fig.1. B,D',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(2)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_3':
        {
            'variant': 'Fig.2. A,C',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_4':
        {
            'variant': 'Fig.2. B,D',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(4)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_5':
        {
            'variant': 'Fig.3. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(5)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_6':
        {
            'variant': 'Fig.3. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(6)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_7':
        {
            'variant': 'Fig.3. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(7)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_8':
        {
            'variant': 'Fig.3. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(8)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_9':
        {
            'variant': 'Fig.3. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(9)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_10':
        {
            'variant': 'Fig.3. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(10)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_11':
        {
            'variant': 'Fig.4. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(11)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_12':
        {
            'variant': 'Fig.4. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(12)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_13':
        {
            'variant': 'Fig.4. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(13)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_14':
        {
            'variant': 'Fig.4. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(14)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_15':
        {
            'variant': 'Fig.4. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(15)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_16':
        {
            'variant': 'Fig.4. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(16)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_17':
        {
            'variant': 'Fig.5. A-C Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(17)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_18':
        {
            'variant': 'Fig.5. A-C Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(18)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_19':
        {
            'variant': 'Fig.5. D Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(19)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_20':
        {
            'variant': 'Fig.5. D Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(20)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_21':
        {
            'variant': 'Fig.5. E-G Symmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(21)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '19214_22':
        {
            'variant': 'Fig.5. E-G Asymmetric',
            'compile': ['cd geomindu', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Main(22)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr geomindu']
        },
    '136026_1':
        {
            'variant': 'Passive tuft, control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.BOTHCONTROL)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_2':
        {
            'variant': 'Passive tuft, cm = 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.CMx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_3':
        {
            'variant': 'Passive tuft, Ra = 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.RAx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_4':
        {
            'variant': 'Passive tuft, both 2*control',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_spiketuft.hoc")', 'h.setparams(h.BOTHx2)', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '136026_5':
        {
            'variant': 'Active tuft',
            'compile': ['cd djurisic2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("init_active.hoc")', 'h.doit()'],
            'cleanup': ['cd ../', 'rm -fr djurisic2008']
        },
    '7399':
        {
            'compile': ['cd lytton98', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.sim_panel()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr na8st']
        },
    '128079':
        {
            'compile': ['cd na8st', 'nrnivmodl mod/'],
            'launch': ['nrngui -python'],
            'run': ['execfile("ap.py")'],
            'cleanup': ['cd ../', 'rm -fr na8st']
        },
    '113997_1':
        {
            'variant': 'HPGA non-saturating',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_non-saturating.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '113997_2':
        {
            'variant': 'HPGA non-saturating (no Ih)',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_non-saturating_noIh.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '113997_3':
        {
            'variant': 'HPGA saturating',
            'compile': ['cd HAGPA', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("demo_HPGA_saturating.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr HAGPA']
        },
    '144376_1':
        {
            'variant': 'HPGA non-saturating',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['execfile("demo_HPGA_non_saturating.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '144376_2':
        {
            'variant': 'HPGA non-saturating (no Ih)',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['execfile("demo_HPGA_non_saturating_noIh.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '144376_3':
        {
            'variant': 'HPGA saturating',
            'compile': ['cd Skolnik_python_WinogradEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['execfile("demo_HPGA_saturating.py")'],
            'cleanup': ['cd ../', 'rm -fr Skolnik_python_WinogradEtAl2008']
        },
    '62266':
        {
            'compile': ['cd b1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr b1']
        },
    '138379':
        {
            'compile': ['cd fdemo', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.mytstop=20e3', 'h.finish_run()'],
            'cleanup': ['cd ../', 'rm -fr fdemo']
        },
    '18197_1':
        {
            'variant': 'fig 1A (Glutamate)',
            'compile': ['cd Neural_Computation', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_glutamate_neuralcomputation")'],
            'cleanup': ['cd ../', 'rm -fr Neural_Computation']
        },
    '18197_2':
        {
            'variant': 'fig 1D (GABA)',
            'compile': ['cd Neural_Computation', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("demo_gaba_neuralcomputation")'],
            'cleanup': ['cd ../', 'rm -fr Neural_Computation']
        },
    '143114_1':
        {
            'variant': 'Synaptic Input',
            'compile': ['cd ZhouColburn2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("LSO_synaptic_input.hoc")', 'h.rerun()'],
            'cleanup': ['cd ../', 'rm -fr ZhouColburn2010']
        },
    '143114_2':
        {
            'variant': 'Current Input',
            'compile': ['cd ZhouColburn2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("LSO_current_input.hoc")', 'h.rerun()'],
            'cleanup': ['cd ../', 'rm -fr ZhouColburn2010']
        },
    '3798_1':
        {
            'variant': 'A',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.unmyl()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_2':
        {
            'variant': 'B',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.5e-3)', 'h.unmyl()', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_3':
        {
            'variant': 'C',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.demyl1(1, 3)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '3798_4':
        {
            'variant': 'D',
            'compile': ['cd shrager91', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.inter_fhdens(0.4e-3)', 'h.demyl1(1, 19)', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr shrager91']
        },
    '19491':
        {
            'compile': ['cd EurJNeurosci2000', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr EurJNeurosci2000']
        },
    '113446':
        {
            'compile': ['cd NEURON-2008b', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr NEURON-2008b']
        },
    '117459':
        {
            'compile': ['cd CruzEtAlS_cellModel', 'nrnivmodl plus5HT/3cell'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CruzEtAlS_cellModel']
        },
    '53435_1':
        {
            'variant': 'Real EPSP',
            'compile': ['cd anyas2005/model_bf_real_EPSP', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '53435_2':
        {
            'variant': 'HPP',
            'compile': ['cd anyas2005/model_bf_HPP', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr anyas2005']
        },
    '112086_1':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("metal()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_2':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("cntel()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },
    '112086_3':
        {
            'variant': 'Metal electrode',
            'compile': ['cd giuglianoEtAl2007', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("cntel2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr giuglianoEtAl2007']
        },

    '37856_1':
        {
            'variant': 'Fig 2',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runiv()")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_2':
        {
            'variant': 'Fig 3A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_3':
        {
            'variant': 'Fig 3B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_4':
        {
            'variant': 'Fig 4A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_5':
        {
            'variant': 'Fig 4B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,1,0)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_6':
        {
            'variant': 'Fig 10A',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,0,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37856_7':
        {
            'variant': 'Fig 10B',
            'compile': ['cd CN_Pyr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("runhyp(1,1,0,1)")'],
            'cleanup': ['cd ../', 'rm -fr CN_Pyr']
        },
    '37857_1':
        {
            'variant': 'Figure2A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_2':
        {
            'variant': 'Figure2B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_3':
        {
            'variant': 'Figure2C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_4':
        {
            'variant': 'Figure2D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig2D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_5':
        {
            'variant': 'Panel A',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_6':
        {
            'variant': 'Panel B',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_7':
        {
            'variant': 'Panel C',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_8':
        {
            'variant': 'Panel D',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig3D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_9':
        {
            'variant': 'Type I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4A()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_10':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4B()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_11':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4C()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_12':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Fig4D()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_13':
        {
            'variant': 'Type I-c',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type1c()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_14':
        {
            'variant': 'Type I-t',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type1t()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_15':
        {
            'variant': 'Type I-II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type12()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_16':
        {
            'variant': 'Type II-I',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type21()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_17':
        {
            'variant': 'Type II',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type2()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '37857_18':
        {
            'variant': 'Type IIo (Octopus)',
            'compile': ['cd CN_Bushy_Stellate', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("Type2o()")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr CN_Bushy_Stellate']
        },
    '35358':
        {
            'compile': ['cd b04feb12', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../', 'rm -fr b04feb12']
        },
    '136176':
        {
            'compile': ['cd Katona_et_al', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ../', 'rm -fr Katona_et_al']
        },
    '138205':
        {
            'compile': ['cd Schizophr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h("display_cell()")'],
            'cleanup': ['cd ../', 'rm -fr Schizophr']
        },
    '144490':
        {
            'compile': ['cd bpap', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.gui_run_bpap()'],
            'cleanup': ['cd ../', 'rm -fr bpap']
        },
    '143719':
        {
            'compile': ['cd Ca1_Bianchi/experiment', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../../', 'rm -fr Ca1_Bianchi']
        },

    '20212_1':
        {
            'variant': 'Disperse 6_2',
            'compile': ['cd CA1_multi/experiment/cluster-dispersion', 'nrnivmodl ../../mechanism', 'chmod +x newshiftsyn', 'export PATH=.:$PATH'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Disperse_6_2.hoc")'],
            'cleanup': ['cd ../../..', 'rm -fr CA1_multi']
        },
    '44050_1':
        {
            'variant': 'Control',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_2':
        {
            'variant': 'AMPA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runa()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '44050_3':
        {
            'variant': 'AMPA + NMDA',
            'compile': ['cd gaspiriniEtAl2004', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr gaspiriniEtAl2004']
        },        
    '144541_1':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig-5a.hoc")', 'h.loop()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },        
    '144541_2':
        {
            'variant': 'Control',
            'compile': ['cd Ih_current', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig-5a.hoc")', 'h.zd()'],
            'cleanup': ['cd ..', 'rm -fr Ih_current']
        },
    '151949':
        {
            'compile': ['cd SousaEtAl2014', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr SousaEtAl2014']
        },
    '7509':
        {
            'compile': ['cd magee2000'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr magee2000'],
            'stopmidsim': False       # need this because an xpanel is open until after the sim completes
        },
    '106551':
        {
            'compile': ['cd nc-mri', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runm()'],
            'cleanup': ['cd ..', 'rm -fr nc-mri']
        },
    '3507':
        {
            'compile': ['cd fh', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fh']
        },
    '7386':
        {
            'compile': ['cd boosting', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runc()'],
            'cleanup': ['cd ..', 'rm -fr boosting']
        },
    '125152':
        {
            'compile': ['cd Uebachs-et-al_2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr Uebachs-et-al_2010']
        },
    '2796_1':
        {
            'variant': 'Fig 1A',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig_1a.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '2796_2':
        {
            'variant': 'Fig 1C',
            'compile': ['cd ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("fig_1c.hoc")', 'h.runu()'],
            'cleanup': ['cd ..', 'rm -fr ca1']
        },        
    '144401':
        {
            'compile': ['cd VladimirovTuTraub2012', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr VladimirovTuTraub2012']
        },
    '87546':
        {
            'compile': ['cd olm-int', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr olm-int']
        },
    '20015':
        {
            'compile': ['cd k_interneurons', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("kinetics.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr k_interneurons']
        },
    '32992':
        {
            'compile': ['cd synchro-ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr synchro-ca1']
        },
    '2937_1':
        {
            'variant': 'Fig 3',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run3()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_2':
        {
            'variant': 'Fig 4bc',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run4bc()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '2937_3':
        {
            'variant': 'Fig 4bd',
            'compile': ['cd slowinact', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run4bd()'],
            'cleanup': ['cd ..', 'rm -fr slowinact']
        },        
    '139418_1':
        {
            'variant': 'Fig 11',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("figure11.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '139418_2':
        {
            'variant': 'Fig 13',
            'compile': ['cd fietkiewicz2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("figure13.hoc")'],
            'cleanup': ['cd ..', 'rm -fr fietkiewicz2011']
        },        
    '46839':
        {
            'compile': ['cd GranuleCell', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr GranuleCell']
        },
    '116830':
        {
            'compile': ['cd b08dec23', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("init.hoc")'],
            'cleanup': ['cd ..', 'rm -fr b08dec23']
        },
    '125689':
        {
            'compile': ['cd CarvalhoBuonomano/Neuron2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.MULTI()'],
            'cleanup': ['cd ../..', 'rm -fr CarvalhoBuonomano']
        },
    '127388':
        {
            'compile': ['cd BGnet', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim()'],
            'cleanup': ['cd ../..', 'rm -fr BGnet']
        },
    '136803':
        {
            'compile': ['cd JonesEtAl2009', 'nrnivmodl mod_files'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ../..', 'rm -fr JonesEtAl2009']
        },
    '116096_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -100', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = -10', 'h.set_axis_limits(0.0014, 0.007, 0.7, 0.35)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },        
    '116096_3':
        {
            'variant': 'Fig 2C',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 10', 'h.set_axis_limits(0.0045, 0.5, 0.9, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '116096_4':
        {
            'variant': 'Fig 2D',
            'compile': ['cd badoual_stdp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.ampasyn.delta = 200', 'h.ampasyn.onset = 10', 'h.set_axis_limits(0.0016, 0.016, 0.7, 0.014)', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr badoual_stdp']
        },
    '147538_1':
        {
            'variant': 'Fig 2A',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Fig2A()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '147538_2':
        {
            'variant': 'Fig 2B',
            'compile': ['cd NarayananJohnston2010', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.Fig2B()'],
            'cleanup': ['cd ..', 'rm -fr NarayananJohnston2010']
        },
    '112834':
        {
            'compile': ['cd nacb_msp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr nacb_msp']
        },
    '125378':
        {
            'compile': ['cd leeEtAl2003', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig8b()'],
            'cleanup': ['cd ..', 'rm -fr leeEtAl2003']
        },
    '115356':
        {
            'compile': ['cd RoyeckEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run_sim_graph()'],
            'cleanup': ['cd ..', 'rm -fr RoyeckEtAl2008']
        },
    '127021':
        {
            'compile': ['cd Golgi_cell_NaKATPAse', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.recreate()'],
            'cleanup': ['cd ..', 'rm -fr Golgi_cell_NaKATPAse']
        },
    '147514':
        {
            'compile': ['cd dendritic_complexity', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr dendritic_complexity']
        },
    '135838':
        {
            'compile': ['cd Alle_et_al_2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Alle_et_al_2009']
        },
    '143635':
        {
            'compile': ['cd CasaleEtAl2011', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.measure()'],
            'cleanup': ['cd ..', 'rm -fr CasaleEtAl2011']
        },
    '87473':
        {
            'compile': ['cd weaver_SimAnn_ObjFcn', 'nrnivmodl model optmz'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr weaver_SimAnn_ObjFcn']
        },
    '135839':
        {
            'compile': ['cd McCormickEtAl2007YuEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
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
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MoradiEtAl2012']
        },
    '28316_1':
        {
            'variant': '8A Long',
            'compile': ['cd OLMmodel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("initFig8Along")'],
            'cleanup': ['cd ..', 'rm -fr OLMmodel']
        },
    '3785_1':
        {
            'variant': 'Figure 3 1A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h.fig1A_vitro()'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_2':
        {
            'variant': 'Figure 4 2A in vitro',
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("mcab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_3':
        {
            'variant': "Figure 4 2A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(1)', 'h("ecab[0] othervitro(10000)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_4':
        {
            'variant': "Figure 5 3A in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("mcab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '3785_5':
        {
            'variant': "Figure 5 3A' in vitro",
            'compile': ['cd crane2001', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.cvode_active(0)', 'h("ecab[0] othervitro(100)")'],
            'cleanup': ['cd ..', 'rm -fr crane2001']
        },
    '87284_1':
        {
            'variant': 'Figure 1, 2',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig1and2()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_2':
        {
            'variant': 'Figure 3',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_3':
        {
            'variant': 'Figure 4',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig4()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_4':
        {
            'variant': 'Figure 5',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig5()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '87284_5':
        {
            'variant': 'Figure 6',
            'compile': ['cd CA1_abeta', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig6()'],
            'cleanup': ['cd ..', 'rm -fr CA1_abeta']
        },
    '18198_1':
        {
            'variant': 'Synaptic Release',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("release")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_2':
        {
            'variant': 'AMPA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ampa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_3':
        {
            'variant': 'AMPA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("ampa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_4':
        {
            'variant': 'NMDA - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("nmda")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_5':
        {
            'variant': 'NMDA - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("nmda5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_6':
        {
            'variant': 'GABA_A - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_7':
        {
            'variant': 'GABA_A - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabaa5")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_8':
        {
            'variant': 'GABA_B - simple',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabab")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '18198_9':
        {
            'variant': 'GABA_B - detailed',
            'compile': ['cd SYN_NEW', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("gabab3")'],
            'cleanup': ['cd ..', 'rm -fr SYN_NEW']
        },
    '136715_1':
        {
            'variant': 'Fig 6B',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig6B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_2':
        {
            'variant': 'Fig 4B 10APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 10APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_3':
        {
            'variant': 'Fig 4B 100APs',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig4B 100APs ver7a.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '136715_4':
        {
            'variant': 'Fig 3A',
            'compile': ['cd FleidervishEtAl2010', 'nrnivmodl MechanismsVer7.1/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.load_file("Fig3A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FleidervishEtAl2010']
        },
    '93321_1':
        {
            'variant': 'Fig 3A (top left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3topleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_2':
        {
            'variant': 'Fig 3B (top right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3topright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_3':
        {
            'variant': 'Fig 3A middle (left)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3middleleft()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_4':
        {
            'variant': 'Fig 3B middle (right)',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'stopmidsim': False,
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3middleright()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '93321_5':
        {
            'variant': 'Fig 3 bottom',
            'compile': ['cd liuEtAl1998', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.fig3bottom()'],
            'cleanup': ['cd ..', 'rm -fr liuEtAl1998']
        },
    '123897_1':
        {
            'variant': 'Pyramidal Cell',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/Pyramidal_Main.hoc")', 'h.freePlay()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_2':
        {
            'variant': 'Uniform Axon',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/UniformAxon_Main.hoc")'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '123897_3':
        {
            'variant': 'Single Compartment (activation)',
            'compile': ['cd HuEtAl2009', 'nrnivmodl mechanism/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.xopen("experiment/SingleComp_Main.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr HuEtAl2009']
        },
    '19176_1':
        {
            'variant': 'Current Steps',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.experiment1()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '19176_2':
        {
            'variant': 'cAMP pulse',
            'compile': ['cd HCN2k', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.experiment2()'],
            'cleanup': ['cd ..', 'rm -fr HCN2k']
        },
    '124063':
        {
            'compile': ['cd PublioEtAl2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.start()'],
            'cleanup': ['cd ..', 'rm -fr PublioEtAl2009']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_1':
        {
            'variant': 'Fig 7C: hh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_2':
        {
            'variant': 'Fig 7C: hh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-hh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },
    '54903_3':
        {
            'variant': 'Fig 7C: NaCh-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_4':
        {
            'variant': 'Fig 7C: NaCh-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_5':
        {
            'variant': 'Fig 7C: NaCh-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-NaCh-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_6':
        {
            'variant': 'Fig 7C: naf-black_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-black_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_7':
        {
            'variant': 'Fig 7C: naf-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_8':
        {
            'variant': 'Fig 7C: naf-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naf-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_9':
        {
            'variant': 'Fig 7C: naxn-black',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-black.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_10':
        {
            'variant': 'Fig 7C: naxn-dark grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-dark grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_11':
        {
            'variant': 'Fig 7C: naxn-light grey_bar',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7C-naxn-light grey_bar.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_12':
        {
            'variant': 'Fig 7D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_13':
        {
            'variant': 'Fig 7E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7E.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_14':
        {
            'variant': 'Fig 6B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_15':
        {
            'variant': 'Fig 6C',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-C.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_16':
        {
            'variant': 'Fig 7B',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7B.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_17':
        {
            'variant': 'Fig 6D',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_18':
        {
            'variant': 'Fig 6E',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-D.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_19':
        {
            'variant': 'Fig 6F',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-F.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_20':
        {
            'variant': 'Fig 7A',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig7A.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '54903_21':
        {
            'variant': 'Fig 6B-inset',
            'compile': ['cd Hossain', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("Fig6-B-inset.ses")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr Hossain']
        },    
    '126637_2c':
        {
            'variant': 'Fig 2C + 2E',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_spine and spine neck at spinydendrite133.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_2d':
        {
            'variant': 'Fig 2D + 2F',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_reduced_PPR model.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_cvode':
        {
            'variant': 'CVODE or other solvers',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit_reduced_PPR model_cvode.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '146026_ex1':
        {
            'variant': 'Example 1',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("example1.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex2':
        {
            'variant': 'Example 2',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("example2.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex3':
        {
            'variant': 'Example 3',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("example3.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '137259':
        {
            'compile': ['cd ca3-synresp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr ca3-synresp']
        },
    '53869':
        {
            'compile': ['cd MSO_Zhouetal_2005', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("MSO_Zhouetal_2005")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MSO_Zhouetal_2005']
        },
    '125857_2frb':
        {
            'variant': '2FRB',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("2FRB")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '140249_a1':
        {
            'variant': 'Fig 4 A1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP1MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b1':
        {
            'variant': 'Fig 4 B1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP1HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_a2':
        {
            'variant': 'Fig 4 A2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP2MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b2':
        {
            'variant': 'Fig 4 B2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.runP2HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },        
    '125857_frb3':
        {
            'variant': 'FRB3',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB3")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_19':
        {
            'variant': 'FRB_12_19',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_19")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_21':
        {
            'variant': 'FRB_12_21',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_21")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '150240':
        {
            'compile': ['cd TCconvergenceModel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h, gui', 'h.load_file("mosinit.hoc")'],
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
