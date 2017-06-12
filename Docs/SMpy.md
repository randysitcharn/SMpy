SMpy.e_factor(EF=None,q=None)

	Compute the next E-factor.

	Parameters :
		EF : Current E-factor
		q  : quality of response

	Returns :
		next E-factor : float
			If no arguments returns 2.5 (the initial value) else returns the computation of E-factor.

	Examples :
		>>> SMpy.e_factor()
		2.5
		
		>>> SMpy.e_factor(EF=2,q=1)
		1.46	


SMpy.inter_repetition(n=None,EF=None,I=None)

	Compute the next interval of repetition

	Parameters :
		n  : number of times the card had been seen since the beginning or a restart of repetition
		EF : Next E-factor (see SMpy.e_factor())
		I  : Current interval of repetition

	Returns :
		next interval of repetition : float
			can accept n alone or the couple EF and I

	Examples :
		>>> SMpy.inter_repetition(n=2)
		6.0
		
		>>> SMpy.inter_repetition(EF=1.46,I=3)
		4.0