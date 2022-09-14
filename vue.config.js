const path = require('path');
const PrerenderSpaPlugin = require('prerender-spa-plugin');

const productionPlugins = [
  new PrerenderSpaPlugin({
    staticDir: path.join(__dirname, 'dist'),
    routes: ['/', '/selection', '/alllist', '/todolist', '/completelist'], // 해당 URL을 프리렌더링함
    renderer: new PrerenderSpaPlugin.PuppeteerRenderer({
      renderAfterElementExists: '#app',
    }),
  }),
];

module.exports = {
  outputDir: process.env.VUE_APP_API_BUILD_PATH, // 배포경로
  lintOnSave: false, // Eslint 끄기
  // 로컬 테스트시 프록시로 /api라는 요청이 오면 이를 플라스크서버(5000번)로 보낸다
  devServer: {
    proxy: {
      '/api*': {
        // changeOrigin는 CORS위반을 막기 위해 서버의 URI(http://127.0.0.1:5000)로 출처를 바꿈
        target: process.env.VUE_APP_API_HOME_URL,
        changeOrigin: true,
      },
    },
  },
  // 프리렌더링설정을 웹팩에 적용
  configureWebpack: (config) => {
    if (process.env.NODE_ENV === 'production') {
      config.plugins.push(...productionPlugins);
    }
  },
};
