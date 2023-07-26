# RFI-Loc
## A python based software that can be used to localize possible RFI sources
We have developed a powerful tool designed to localize and identify sources of intermittent broadband radio frequency interference (RFI) near GMRT using routine observation data.

At its core, the tool utilizes the concept of fringe patterns, generated when a broadband source is detected by both antennas of a single baseline. These fringe patterns exhibit sinusoidal variations in visibility intensity across frequencies. By performing a Fourier transform on the visibility data along the frequency axis, we obtain delay measurements representing the propagation delay between the source and each antenna. Each delay corresponds to a hyperbola connecting two antennas.

With GMRT boasting around 26-28 operational antennas at any given time, we gather multiple hyperbolas from numerous baselines. For a common RFI source, these hyperbolas intersect, facilitating the identification of the source.

The tool has a Python-based user interface, enabling users to efficiently locate and mark RFI sources on the observation data. Additionally, it provides the functionality to save the identified sources to a database for future reference and analysis.

We believe this tool will greatly assist astronomers and radio engineers in their efforts to study and mitigate RFI, contributing to a deeper understanding of celestial phenomena observed through the GMRT telescope.
![image](https://github.com/riyagori1203/RFI-Loc/assets/66380988/78779284-6820-494c-89f6-6b21eeff596b)
