module.exports = {
  lintOnSave: false, // Eslint 끄기
  // 프록시로 /api라는 요청이 오면 이를 플라스크서버(5000번)로 보낸다
  devServer: {
    proxy: {
      '/api*': {
        // changeOrigin는 CORS위반을 막기 위해 서버의 URI(http://localhost:5000)로 출처를 바꿈
        target: 'http://localhost:5000/api',
        changeOrigin: true,
      },
    },
  },
};
