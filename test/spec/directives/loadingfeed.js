'use strict';

describe('Directive: loadingFeed', function () {

  // load the directive's module
  beforeEach(module('quickNewsApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<loading-feed></loading-feed>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('LOADING...');
  }));
});
