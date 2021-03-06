"""Default settings dictionary.

This is the default settings dictionary. There's nothing special about these
parameters, but they reflect measured or good-guess vaules. These values will
allow the simulation to run but should be modified for specific simulations

See the documentation for "settings_blank_template.py" to modify these
parameters at runtime.

The references for each value are indicated and listed below.

"""

from equations import neuron_eqs, synapse_eqs, onspike_eqs, sinusoid_rate


settings = {
    "neurons": {
        "HVA_PY": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.030,      # (2)
            "tau_e": 0.002,      # (2)
            "tau_i": 0.010,      # (2)
            "thresh": -0.044,    # (4)
            "reset": -0.050,     # measured in lab
            "V_rest": -0.075,    # (4)
            "refract": 0.0015
        },

        "FS": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.010,      # (1)
            "tau_e": 0.002,      # (6)
            "tau_i": 0.008,      # (6)
            "thresh": -0.040,    # (4)
            "reset": -0.058,     # (2)
            "V_rest": -0.071,    # (4)
            "refract": 0.0015
        },

        "SOM": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.026,      # (1)
            "tau_e": 0.002,      # (2)
            "tau_i": 0.012,      # (1)
            "thresh": -0.040,    # (5)
            "reset": -0.055,     # measured in lab
            "V_rest": -0.060,    # (5)
            "refract": 0.0015
        }
    },

    "afferents": {
        "N": 800,
        "use_poisson": True,
        "modulation_rate": [5],
        "peak_rate": 50,
        "spikes_per_second": None,
        "eqs": sinusoid_rate,
        "sim_time": 2
    },

    "synapses": {
        ("SOM", "HVA_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0,
            "d1": 0.5,
            "d2": 1.0,
            "f1": 0.0,
            "f2": 0.0,
            "tau_D1": 0.300,
            "tau_D2": 0.300,
            "tau_F1": 0.300,
            "tau_F2": 0.300,
            "w_e": 0.00,
            "w_i": 0.0025,
            "delay": 0
        },

        ("FS", "HVA_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0,
            "d1": 0.4,
            "d2": 1.0,
            "f1": 0.0,
            "f2": 0.0,
            "tau_D1": 0.300,
            "tau_D2": 0.300,
            "tau_F1": 0.300,
            "tau_F2": 0.300,
            "w_e": 0.00,
            "w_i": 0.005,
            "delay": 0
        },

        ("afferents", "HVA_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0.6,
            "d1": 0.7,
            "d2": 1.0,
            "f1": 0.0,
            "f2": 0.0,
            "tau_D1": 0.200,
            "tau_D2": 0.300,
            "tau_F1": 1000,
            "tau_F2": 0.300,
            "w_e": 0.010,
            "w_i": 0.00,
            "delay": 0
        },

        ("afferents", "FS"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0.6,
            "d1": 0.4,
            "d2": 1.0,
            "f1": 0.0,
            "f2": 0.0,
            "tau_D1": 0.300,
            "tau_D2": 0.300,
            "tau_F1": 1000,
            "tau_F2": 0.300,
            "w_e": 0.015,
            "w_i": 0.00,
            "delay": 0
        },

        ("afferents", "SOM"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0.6,
            "d1": 1.0,
            "d2": 1.0,
            "f1": 0.7,
            "f2": 0.0,
            "tau_D1": 0.400,
            "tau_D2": 0.300,
            "tau_F1": 0.400,
            "tau_F2": 0.300,
            "w_e": 0.002,
            "w_i": 0.00,
            "delay": 0
        }
    },

    "monitors": {
        "HVA_PY": 'V Ge_total Gi_total',
        "FS": 'V Ge_total Gi_total',
        "SOM": 'V Ge_total Gi_total',
        "afferents": 'spikes'
    }
}

#####################################
# References
# 1. "Supralinear increase of recurrent inhibition during sparse
#       activity in somatosensory cortex" (2007)
#       Kapfer, Glickfeld, Atallah, Scanziani
# 2. "Synaptic Depression and the Temporal Response Characteristics
#       of V1 Cells" (1998)
#       Chance, Nelson, Abbott
# 3. "The Excitatory Neuronal Network of the C2 Barrel Column in Mouse
#       Primary Somatosensory Cortex" (2008)
#       Lefort, Tomm, Sarria, Peterson
# 4. "Distinct Balance of excitation and inhjibition in an intrareal
#       feedforward and feedback circuit of mouse visual cortex" (2013)
#       Yang, Carrasquillo, Hooks, Nerbonne, Burkhalter
# 5. "Diveristy and overlap of parvalbumin and somatostatin expressing neurons
#       in mouse presubiculum" (2015)
#       Nassar et al.
# 6. "Membrane Properties and the Balance between Excitation and Inhibition
#       Control Gamma-Frequency Oscillations Arising from Feedback Inhibition"
#       (2012)
#       Economo, White
#
