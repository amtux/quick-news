'use strict';

describe('Controller: BbcCtrl', function () {

  // load the controller's module
  beforeEach(module('quickNewsApp'));

  var BbcCtrl, scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) { 
    scope = $rootScope.$new();
    BbcCtrl = $controller('BbcCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(BbcCtrl.awesomeThings.length).toBe(3);
  });
});

