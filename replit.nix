{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.python310Packages.flask
    pkgs.git
  ];
  env = {
    PYTHONPATH = "$PYTHONPATH:/home/runner/${REPL_SLUG}";
  };
}