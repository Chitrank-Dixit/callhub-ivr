(function () {
  'use strict';

  angular
    .module('app', [
      'app.config',
      'app.routes',
      'app.accounts',
      'app.authentication',
      'app.layout',
      'app.posts',
      'app.utils'
    ]);

  angular
    .module('app.config', []);

  angular
    .module('app.routes', ['ngRoute']);

  angular
    .module('app')
    .run(run);

  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
