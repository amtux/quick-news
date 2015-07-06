'use strict';

describe('Controller: NavCtrl', function () {

  // load the controller's module
  beforeEach(module('quickNewsApp'));

  var NavCtrl;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    NavCtrl = $controller('NavCtrl', {
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NavCtrl.awesomeThings.length).toBe(3);
  });
});
