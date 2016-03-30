#! python3

################################ PYTHON FUNCTIONS 2016.03.30





################################################## INSTALL THE REQUIRED PACKAGES
def install_required_packages(packages):
    # Import the pip library to install packages inside the script
    import pip
    ############### Upgrade the existing packages
    # Retrieve the list of installed packages
    #installed_packages = pip.get_installed_distributions()
    # Keep only the packages
    #for i in range(len(installed_packages)):
    #    installed_packages[i] = str(installed_packages[i])
    #    installed_packages[i] = installed_packages[i].split()[0].lower()
    # Upgrade the installed packages
    #if len(installed_packages) > 0:
    #    for pkg in installed_packages:
    #        pip.main(["install", "--upgrade", pkg])
    ############### Install the new packages
    ##### Retrieve the list of installed packages
    installed_packages = pip.get_installed_distributions()
    # Keep only the packages
    for i in range(len(installed_packages)):
        installed_packages[i] = str(installed_packages[i])
        installed_packages[i] = installed_packages[i].split()[0].lower()
    # Determine the packages to be installed
    packages_to_be_installed = []
    ##### Convert the input packages in lowercase
    # List of packages
    if type(packages) is list:
        # Lowercase
        for p in range(len(packages)):
            packages[p] = packages[p].lower()
        # Add the missing packages to the list of packages to be installed
        for package in packages:
            if package not in installed_packages:
                packages_to_be_installed.append(package)
    elif type(packages) is str:
        # Lowercase
        packages = packages.lower()
        # Add the missing packages to the list of packages to be installed
        if packages not in installed_packages:
            packages_to_be_installed.append(packages)
    # Install the packages
    if len(packages_to_be_installed) > 0:
        for pkg in range(len(packages_to_be_installed)):
            pip.main(["install", packages_to_be_installed[pkg]])





################################################################################





####################################################### READ THE SPECTRA (imzML)
def import_spectra(filepath, spectra_format="imzml"):
    ############### IMZML
    if spectra_format == "imzml" or spectra_format == "imzML":
        ##### Import the libraries
        install_required_packages("pyimzml")
        from pyimzml.ImzMLParser import ImzMLParser
        ##### Parse the imzML file
        parsed_imzml = ImzMLParser(filepath)
        ##### Generate the list of spectra
        spectra = []
        for i,(x,y) in enumerate(parsed_imzml.coordinates):
            spectra.append(parsed_imzml.getspectrum(i))
    ############### XMASS
    elif spectra_format == "brukerflex" or spectra_format == "xmass" or spectra_format == "Xmass":
        pass
    ############### Return the list of spectra
    return (spectra)





################################################################################











def molecular_image(spectra):
    # Import the libraries
    install_required_packages("pyimzml","matplotlib")
    from pyimzml.ImzMLParser import ImzMLParser
    from pyimzml.ImzMLParser import getionimage
    import matplotlib.pyplot as plt
    ##### Parse the imzML file
    parsed_imzml = ImzMLParser(filepath)
    # Pick a base peak
    mzA, intA = spectra[0]
    peakMz = mzA[intA.index(max(intA))]
    # Show the image
    im = getionimage(spectra, peakMz)
    plt.imshow(im).set_interpolation('nearest')
    plt.colorbar()
    plt.show()
