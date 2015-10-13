Feature: Activity

  Scenario: Authorization verification

     When action target not found
       Then it should fail when action target not found

	 When action target found
       Then it should fail when target type not matching

	   When deny role found
	     When deny role found once
           Then it should fail when principal match the deny role definition
	       Then it should fail when principal and extra info match the deny role definition
	       Then it should succeed when principal does not match every deny role definition in a set
	       Then it should fail when principal match every deny role definition in a set
	       Then it should fail when a matching deny role definition does not define a "contains" method
		   Then it should fail when a matching deny role definition has a "contains" method that does not take at least one parameter
		   Then it should fail when a matching deny role definition has a "contains" method that does not return a boolean value
	     
	     When deny role found more than once
	       Then it should fail when principal and any extra info match any deny role definition
	       Then it should fail when principal and any extra info match any contained deny role definition
	       Then it should fail when principal and any extra info match any deny role definition in an embedded container action

	   When deny role not found
	     When allow role not found
		   Then it should fail when allow role not found

		 When allow role found
		   When allow role found once
		     Then it should succeed when principal match an allow role definition
			 Then it should succeed when principal and extra info match an allow role definition
		     Then it should fail when principal does not match every allow role definition in a set
		     Then it should succeed when principal does match every allow role definition in a set
		     Then it should fail when a matching allow role definition does not define a "contains" method
			 Then it should fail when a matching allow role definition has a "contains" method that does not take at least one parameter
		     Then it should fail when a matching allow role definition has a "contains" method that does not return a boolean value

		   When allow role found more than once
		     Then it should succeed when principal and any extra info match any allow role definition
		     Then it should fail when principal and any extra info do not match any allow role definition
		     Then it should succeed when principal and any extra info match any contained allow role definition
		     Then it should succeed when principal and any extra info match any allow role definition in an embedded container action