module.exports = {
  lintOnSave: false, // Eslint 끄기
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to flask dev server
        target: 'http://localhost:5000/',
      },
    },
  },
};
