(function () {
  'use strict';

  angular
    .module('app.posts', [
      'app.posts.controllers',
      'app.posts.directives',
      'app.posts.services'
    ]);

  angular
    .module('app.posts.controllers', []);

  angular
    .module('app.posts.directives', ['ngDialog']);

  angular
    .module('app.posts.services', []);
})();
