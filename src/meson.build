pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'flatpaksync')
gnome = import('gnome')

gnome.compile_resources('flatpaksync',
  'flatpaksync.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'flatpaksync.in',
  output: 'flatpaksync',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

flatpaksync_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'about.py',
]

install_data(flatpaksync_sources, install_dir: moduledir)


fp_sources = [
  'flatpak/__init__.py',
  'flatpak/flatpakcmd.py'
]
install_data(fp_sources, install_dir: join_paths(moduledir, 'flatpak') )
