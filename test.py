# Add data 
import pandas as pd
# adonis p for diversity & gene copies
adonis_p_div = pd.DataFrame({
    "Cd_level": [0, 2, 5, 15],
    "adonis_p_div": [0.02, 0.191, 0.836, 0.874]
})

# adonis p for CDOM parameters
adonis_p_cdom = pd.DataFrame({
    "Cd_level": [0, 2, 5, 15],
    "adonis_p_cdom": [0.1, 0.041, 0.041, 0.791]
})

# merge by Cd_level
adonis_p_combined = adonis_p_div.merge(adonis_p_cdom, on="Cd_level")

# convert Cd_level to categorical with ordered levels
adonis_p_combined["Cd_level"] = pd.Categorical(
    adonis_p_combined["Cd_level"],
    categories=[0, 2, 5, 15],
    ordered=True
)
adonis_p_combined