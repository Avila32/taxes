class TaxParams(object):
	def __init__(self):
		self.ik = float(1000)
		self.ik_hat = float(1000)
		self.rk = float(900)
		self.t = float(0.13)
		self.pi = float(0.2)
		self.pi2 = float(0.4)
		self.a = float(100)
		self.p_wave = float(0.1)

def saturate(x):
	if (x < 0.): 
		return 0.0
	if (x > 1.):
		return 1.0
	return x		
		

class TaxSolver(TaxParams):
	def solve(self):
		self.rk = min(self.rk, self.ik)
		pk = (self.ik_hat - self.rk) / self.ik_hat
		pk = saturate(pk)
		c2 = self.pi2 * (self.ik - self.rk)
		c1 = self.ik - c2 - self.t * self.rk
		bk = min((1 - self.p_wave) * c2 / 2.0, self.a)
		p_hat = (1.0 / self.a) * bk
		p_hat = saturate(p_hat)
		E1 = self.ik - self.t * self.ik
		E2 = (1 - pk) * (self.ik - self.t * self.rk)
		E3 = self.ik - self.pi * (self.ik - self.rk) - self.t * self.rk
		e1 = c1 + p_hat * ((1 - self.p_wave) * c2 - bk)
		e2 = pk * max(e1, E3)
		e = max(E1, E2 + e2)
		
		#E1 > (e2 + E2), e1 > E3
		if (e1 <= E3):
			bk = 0
		return E1, e, bk
		
	
