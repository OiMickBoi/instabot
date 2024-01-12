{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
        python3
        python311Packages.pip
    ];

shellHook = ''
  source env/bin/activate
'';

}