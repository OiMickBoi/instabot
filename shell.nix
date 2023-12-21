{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
        python3
    ];

shellHook = ''
  source env/bin/activate
'';

}