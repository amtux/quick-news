'use strict';

describe('Controller: CbcCtrl', function () {

  // load the controller's module
  beforeEach(module('quickNewsApp'));

  var CbcCtrl, scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    CbcCtrl = $controller('CbcCtrl', {
      // place here mocked dependencies
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(CbcCtrl.awesomeThings.length).toBe(3);
  });
});
