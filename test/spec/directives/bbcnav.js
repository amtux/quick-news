'use strict';

describe('Directive: bbcNav', function () {

  // load the directive's module
  beforeEach(module('quickNewsApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<bbc-nav></bbc-nav>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the bbcNav directive');
  }));
});
