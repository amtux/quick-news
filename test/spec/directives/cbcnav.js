'use strict';

describe('Directive: cbcNav', function () {

  // load the directive's module
  beforeEach(module('quickNewsApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<cbc-nav></cbc-nav>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the cbcNav directive');
  }));
});
