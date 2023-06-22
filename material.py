class PhongMaterial:
    """
    ka: coefficient of diffused light from the environment
    kd: diffuse reflection coefficient
    ks: specular reflection coefficient
    n: Phong constant
    """
    def __init__(self, ka, kd, ks, n):
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.n = n