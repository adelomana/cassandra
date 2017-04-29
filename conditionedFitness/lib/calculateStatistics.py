import numpy
import scipy
from scipy import stats

def main(a,b):

    # defining the CFUs before and after FOA with/without caffeine
    x_t_o=a[0]
    x_t_f=a[1]
    x_nt_o=b[0]
    x_nt_f=b[1]

    # converting CFUs into relative numbers, or survival. Using the mean value of before treatment
    r_t_o=x_t_o/numpy.mean(x_t_o)
    r_t_f=x_t_f/numpy.mean(x_t_o)
    r_nt_o=x_nt_o/numpy.mean(x_nt_o)
    r_nt_f=x_nt_f/numpy.mean(x_nt_o)
    
    survival_mu_t=r_t_f
    survival_mu_nt=r_nt_f

    print(survival_mu_t,survival_mu_nt)

    survival_var_t = numpy.mean(r_t_f**2)*numpy.mean(r_t_o**2) - (numpy.mean(r_t_f)**2)*(numpy.mean(r_t_o)**2)
    survival_var_nt = numpy.mean(r_nt_f**2)*numpy.mean(r_nt_o**2) - (numpy.mean(r_nt_f)**2)*(numpy.mean(r_nt_o)**2)

    # calculating the cf 
    cf_mu = numpy.mean(survival_mu_t) - numpy.mean(survival_mu_nt)

    n_t = len(x_t_o) + len(x_t_f)
    n_nt = len(x_nt_o) + len(x_nt_f)
    cf_var = (survival_var_t/n_t) + (survival_var_nt/n_nt)
    cf_sd = numpy.sqrt(cf_var)

    # computing the statistical test: Mann-Whitney U
    (statistic, pvalue) = scipy.stats.mannwhitneyu(survival_mu_t, survival_mu_nt)

    return cf_mu, cf_sd, pvalue
