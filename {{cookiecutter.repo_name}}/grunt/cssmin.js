module.exports = {
  target: {
    files: {
      '{{cookiecutter.repo_name}}/static/dist/release.css': [
        '{{cookiecutter.repo_name}}/static/css/build/custom_bootstrap_compilation.css',
        '{{cookiecutter.repo_name}}/static/css/build/project.css',
      ]
    }
  }
}
