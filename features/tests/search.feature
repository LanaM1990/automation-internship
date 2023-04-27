# Created by svetlanamikolenko at 4/20/23
Feature: Cureskin search tests

  Scenario: Search results show the right result
    Given Open main page
    When Close a pop up
    When Click on search icon in the header
    When Input text SPF into search field
    Then Verify results have SPF