let
  pkgs = import ../nix/packages.nix {};
  python38Packages = pkgs.python38Packages;
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.3.0";
  }) {
    pkgs = pkgs;

    # optionally specify the python version
    python = "python38";
    pypiDataRev = "c55a81951312aa8e6a75d4a2d1b28603e3e3ac8e";
    pypiDataSha256 = "0zfhc9w7ij2ifvdwnaxnpi6ad9kw0s0ry02pfjyz16wg90z0ysa2";

  };
  deposit-cli = mach-nix.buildPythonApplication {
    src = builtins.fetchGit{
      url = "https://github.com/ChorusOne/eth2.0-deposit-cli";
      ref = "packaging-fixes";
      rev = "7d18cefb5c550ceca824490fdd912e74a3b3e083";
    };

  };
in
mach-nix.mkPython {
  packagesExtra = [ deposit-cli ];
}