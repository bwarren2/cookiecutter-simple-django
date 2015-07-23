module.exports = {
  development: {
    options: {
      compress: true,
      yuicompress: true,
      optimization: 2,
    },
    files: {
      "{{cookiecutter.repo_name}}/static/css/build/custom_bootstrap_compilation.css":
        "{{cookiecutter.repo_name}}/static/css/custom_bootstrap_compilation.less",
      "{{cookiecutter.repo_name}}/static/css/build/project.css":
        "{{cookiecutter.repo_name}}/static/css/project.less",
      "{{cookiecutter.repo_name}}/static/css/build/variables.css":
        "{{cookiecutter.repo_name}}/static/css/variables.less",
    }
  }
}
