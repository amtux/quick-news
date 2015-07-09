'use strict';

describe('Controller: ReutersCtrl', function () {

  // load the controller's module
  beforeEach(module('quickNewsApp'));

  var ReutersCtrl, scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReutersCtrl = $controller('ReutersCtrl', {
      // place here mocked dependencies
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(ReutersCtrl.awesomeThings.length).toBe(3);
  });
});
