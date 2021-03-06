sampleDataSet = '/QCD_Pt-1400to1800_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM'
sampleCMSEnergy = 7000

sampleRelease = "CMSSW_4_2_2_patch2" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleNumEvents = 2196200

sampleXSec = 0.0109 # cross-section times filter efficiency (pb)

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START42_V13::All'
sampleHLTProcess = '*'

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/QCDem1400"

sampleRecoFiles = [ ]

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_Xh8.root",
  sampleBaseDir+"/pat/PATtuple_2_1_vQK.root",
  sampleBaseDir+"/pat/PATtuple_3_1_3nN.root",
  sampleBaseDir+"/pat/PATtuple_4_1_DIf.root",
  sampleBaseDir+"/pat/PATtuple_5_1_I1V.root",
  sampleBaseDir+"/pat/PATtuple_6_1_rPD.root",
  sampleBaseDir+"/pat/PATtuple_7_1_Dyh.root",
  sampleBaseDir+"/pat/PATtuple_8_1_Pyc.root",
  sampleBaseDir+"/pat/PATtuple_9_1_k05.root",
  sampleBaseDir+"/pat/PATtuple_10_1_Q2U.root",
  sampleBaseDir+"/pat/PATtuple_11_1_trF.root",
  sampleBaseDir+"/pat/PATtuple_12_1_Q0V.root",
  sampleBaseDir+"/pat/PATtuple_13_1_j8k.root",
  sampleBaseDir+"/pat/PATtuple_14_1_STy.root",
  sampleBaseDir+"/pat/PATtuple_15_1_aK8.root",
  sampleBaseDir+"/pat/PATtuple_16_1_K4j.root",
  sampleBaseDir+"/pat/PATtuple_17_1_pqp.root",
  sampleBaseDir+"/pat/PATtuple_18_1_EaA.root",
  sampleBaseDir+"/pat/PATtuple_19_1_hfG.root",
  sampleBaseDir+"/pat/PATtuple_20_1_QpJ.root",
  sampleBaseDir+"/pat/PATtuple_21_1_094.root",
  sampleBaseDir+"/pat/PATtuple_22_1_d3z.root",
  sampleBaseDir+"/pat/PATtuple_23_1_Dgf.root",
  sampleBaseDir+"/pat/PATtuple_24_1_ksu.root",
  sampleBaseDir+"/pat/PATtuple_25_1_Uh8.root",
  sampleBaseDir+"/pat/PATtuple_26_1_usU.root",
  sampleBaseDir+"/pat/PATtuple_27_1_Pkq.root",
  sampleBaseDir+"/pat/PATtuple_28_1_K7X.root",
  sampleBaseDir+"/pat/PATtuple_29_1_loX.root",
  sampleBaseDir+"/pat/PATtuple_30_1_VF6.root",
  sampleBaseDir+"/pat/PATtuple_31_1_8oS.root",
  sampleBaseDir+"/pat/PATtuple_32_1_LPJ.root",
  sampleBaseDir+"/pat/PATtuple_33_1_u3w.root",
  sampleBaseDir+"/pat/PATtuple_34_1_FR9.root",
  sampleBaseDir+"/pat/PATtuple_35_1_mPt.root",
  sampleBaseDir+"/pat/PATtuple_36_1_4rC.root",
  sampleBaseDir+"/pat/PATtuple_37_1_gUl.root",
  sampleBaseDir+"/pat/PATtuple_38_1_1wb.root",
  sampleBaseDir+"/pat/PATtuple_39_1_Lmo.root",
  sampleBaseDir+"/pat/PATtuple_40_1_Ss5.root",
  sampleBaseDir+"/pat/PATtuple_41_1_fYV.root",
  sampleBaseDir+"/pat/PATtuple_42_1_t0p.root",
  sampleBaseDir+"/pat/PATtuple_43_1_M0c.root",
  sampleBaseDir+"/pat/PATtuple_44_1_9EY.root",
  sampleBaseDir+"/pat/PATtuple_45_1_rgG.root",
  sampleBaseDir+"/pat/PATtuple_46_1_Iyk.root",
  sampleBaseDir+"/pat/PATtuple_47_1_oBT.root",
  sampleBaseDir+"/pat/PATtuple_48_1_VXl.root",
  sampleBaseDir+"/pat/PATtuple_49_1_u5E.root",
  sampleBaseDir+"/pat/PATtuple_50_1_WJ9.root",
  sampleBaseDir+"/pat/PATtuple_51_1_sNx.root",
  sampleBaseDir+"/pat/PATtuple_52_1_f1f.root",
  sampleBaseDir+"/pat/PATtuple_53_3_vpX.root",
  sampleBaseDir+"/pat/PATtuple_54_2_xEc.root",
  sampleBaseDir+"/pat/PATtuple_55_1_SVf.root",
  sampleBaseDir+"/pat/PATtuple_56_1_Rgu.root",
  sampleBaseDir+"/pat/PATtuple_57_2_pT3.root",
  sampleBaseDir+"/pat/PATtuple_58_1_kbn.root",
  sampleBaseDir+"/pat/PATtuple_59_1_XG0.root",
  sampleBaseDir+"/pat/PATtuple_60_1_g2Z.root",
  sampleBaseDir+"/pat/PATtuple_61_1_y4E.root",
  sampleBaseDir+"/pat/PATtuple_62_1_e9X.root",
  sampleBaseDir+"/pat/PATtuple_63_1_Jt3.root",
  sampleBaseDir+"/pat/PATtuple_64_1_pfd.root",
  sampleBaseDir+"/pat/PATtuple_65_2_qPV.root",
  sampleBaseDir+"/pat/PATtuple_66_1_Eqh.root",
  sampleBaseDir+"/pat/PATtuple_67_1_tug.root",
  sampleBaseDir+"/pat/PATtuple_68_1_1ZJ.root",
  sampleBaseDir+"/pat/PATtuple_69_1_RD0.root",
  sampleBaseDir+"/pat/PATtuple_70_1_YoP.root",
  sampleBaseDir+"/pat/PATtuple_71_1_4K7.root",
  sampleBaseDir+"/pat/PATtuple_72_1_G3X.root",
  sampleBaseDir+"/pat/PATtuple_73_1_FGl.root",
  sampleBaseDir+"/pat/PATtuple_74_1_plJ.root",
  sampleBaseDir+"/pat/PATtuple_75_1_QiQ.root",
  sampleBaseDir+"/pat/PATtuple_76_1_9aG.root",
  sampleBaseDir+"/pat/PATtuple_77_1_M06.root",
  sampleBaseDir+"/pat/PATtuple_78_2_tsw.root",
  sampleBaseDir+"/pat/PATtuple_79_1_D8c.root",
  sampleBaseDir+"/pat/PATtuple_80_1_sEK.root",
  sampleBaseDir+"/pat/PATtuple_81_1_lBb.root",
  sampleBaseDir+"/pat/PATtuple_82_1_4Fj.root",
  sampleBaseDir+"/pat/PATtuple_83_1_LxP.root",
  sampleBaseDir+"/pat/PATtuple_84_1_5Cx.root",
  sampleBaseDir+"/pat/PATtuple_85_1_mX3.root",
  sampleBaseDir+"/pat/PATtuple_86_1_hcA.root",
  sampleBaseDir+"/pat/PATtuple_87_1_lQT.root",
  sampleBaseDir+"/pat/PATtuple_88_1_4X2.root",
  sampleBaseDir+"/pat/PATtuple_89_1_uFS.root",
  sampleBaseDir+"/pat/PATtuple_90_1_Agk.root",
  sampleBaseDir+"/pat/PATtuple_91_1_exa.root",
  sampleBaseDir+"/pat/PATtuple_92_1_ZjG.root",
  sampleBaseDir+"/pat/PATtuple_93_1_BSR.root",
  sampleBaseDir+"/pat/PATtuple_94_1_bUv.root",
  sampleBaseDir+"/pat/PATtuple_95_1_1Fr.root",
  sampleBaseDir+"/pat/PATtuple_96_1_7wG.root",
  sampleBaseDir+"/pat/PATtuple_97_1_nn0.root",
  sampleBaseDir+"/pat/PATtuple_98_1_jp5.root",
  sampleBaseDir+"/pat/PATtuple_99_1_NO2.root",
  sampleBaseDir+"/pat/PATtuple_100_1_Jiw.root",
  sampleBaseDir+"/pat/PATtuple_101_1_B1A.root",
  sampleBaseDir+"/pat/PATtuple_102_1_PuP.root",
  sampleBaseDir+"/pat/PATtuple_103_1_6rK.root",
  sampleBaseDir+"/pat/PATtuple_104_1_bGz.root",
  sampleBaseDir+"/pat/PATtuple_105_1_oGk.root",
  sampleBaseDir+"/pat/PATtuple_106_1_OMG.root",
  sampleBaseDir+"/pat/PATtuple_107_1_iAc.root",
  sampleBaseDir+"/pat/PATtuple_108_1_8yt.root",
  sampleBaseDir+"/pat/PATtuple_109_1_JzQ.root",
  sampleBaseDir+"/pat/PATtuple_110_1_Hpw.root",
  sampleBaseDir+"/pat/PATtuple_111_1_Xrz.root",
  sampleBaseDir+"/pat/PATtuple_112_1_mc9.root",
  sampleBaseDir+"/pat/PATtuple_113_1_gN0.root",
  sampleBaseDir+"/pat/PATtuple_114_1_wwH.root",
  sampleBaseDir+"/pat/PATtuple_115_1_5ho.root",
  sampleBaseDir+"/pat/PATtuple_116_1_cFp.root",
  sampleBaseDir+"/pat/PATtuple_117_1_1kM.root",
  sampleBaseDir+"/pat/PATtuple_118_1_CCY.root",
  sampleBaseDir+"/pat/PATtuple_119_1_GMT.root",
  sampleBaseDir+"/pat/PATtuple_120_1_whX.root",
  sampleBaseDir+"/pat/PATtuple_121_1_988.root",
  sampleBaseDir+"/pat/PATtuple_122_1_UZY.root",
  sampleBaseDir+"/pat/PATtuple_123_1_oL8.root",
  sampleBaseDir+"/pat/PATtuple_124_1_01j.root",
  sampleBaseDir+"/pat/PATtuple_125_1_sY2.root",
  sampleBaseDir+"/pat/PATtuple_126_1_MLj.root",
  sampleBaseDir+"/pat/PATtuple_127_1_xqJ.root",
  sampleBaseDir+"/pat/PATtuple_128_1_UCT.root",
  sampleBaseDir+"/pat/PATtuple_129_1_TTx.root",
  sampleBaseDir+"/pat/PATtuple_130_1_sY9.root",
  sampleBaseDir+"/pat/PATtuple_131_1_qZ9.root",
  sampleBaseDir+"/pat/PATtuple_132_1_zdK.root",
  sampleBaseDir+"/pat/PATtuple_133_1_xJN.root",
  sampleBaseDir+"/pat/PATtuple_134_1_8k0.root",
  sampleBaseDir+"/pat/PATtuple_135_1_3mz.root",
  sampleBaseDir+"/pat/PATtuple_136_1_EdC.root",
  sampleBaseDir+"/pat/PATtuple_137_1_n9k.root",
  sampleBaseDir+"/pat/PATtuple_138_1_JHZ.root",
  sampleBaseDir+"/pat/PATtuple_139_1_0JI.root",
  sampleBaseDir+"/pat/PATtuple_140_1_wRd.root",
  sampleBaseDir+"/pat/PATtuple_141_1_bhy.root",
  sampleBaseDir+"/pat/PATtuple_142_1_a8L.root",
  sampleBaseDir+"/pat/PATtuple_143_1_yXA.root",
  sampleBaseDir+"/pat/PATtuple_144_1_5nq.root",
  sampleBaseDir+"/pat/PATtuple_145_1_GgW.root",
  sampleBaseDir+"/pat/PATtuple_146_1_WIl.root",
  sampleBaseDir+"/pat/PATtuple_147_1_LYW.root",
  sampleBaseDir+"/pat/PATtuple_148_1_O8s.root",
  sampleBaseDir+"/pat/PATtuple_149_1_7qy.root",
  sampleBaseDir+"/pat/PATtuple_150_1_c9R.root",
  sampleBaseDir+"/pat/PATtuple_151_1_c8y.root",
  sampleBaseDir+"/pat/PATtuple_152_1_v49.root",
  sampleBaseDir+"/pat/PATtuple_153_1_jnc.root",
  sampleBaseDir+"/pat/PATtuple_154_1_UJj.root",
  sampleBaseDir+"/pat/PATtuple_155_1_xQ0.root",
  sampleBaseDir+"/pat/PATtuple_156_1_gFZ.root",
  sampleBaseDir+"/pat/PATtuple_157_1_9yn.root",
  sampleBaseDir+"/pat/PATtuple_158_1_Vvy.root",
  sampleBaseDir+"/pat/PATtuple_159_1_1QR.root",
  sampleBaseDir+"/pat/PATtuple_160_1_12B.root",
  sampleBaseDir+"/pat/PATtuple_161_1_BJ4.root",
  sampleBaseDir+"/pat/PATtuple_162_1_aLk.root",
  sampleBaseDir+"/pat/PATtuple_163_1_EvO.root",
  sampleBaseDir+"/pat/PATtuple_164_1_xCk.root",
  sampleBaseDir+"/pat/PATtuple_165_1_inA.root",
  sampleBaseDir+"/pat/PATtuple_166_1_2tT.root",
  sampleBaseDir+"/pat/PATtuple_167_1_71Q.root",
  sampleBaseDir+"/pat/PATtuple_168_1_Nbp.root",
  sampleBaseDir+"/pat/PATtuple_169_1_d1E.root",
  sampleBaseDir+"/pat/PATtuple_170_1_W25.root",
  sampleBaseDir+"/pat/PATtuple_171_1_bjy.root",
  sampleBaseDir+"/pat/PATtuple_172_1_lXf.root",
  sampleBaseDir+"/pat/PATtuple_173_1_pGH.root",
  sampleBaseDir+"/pat/PATtuple_174_1_1gX.root",
  sampleBaseDir+"/pat/PATtuple_175_1_t5P.root",
  sampleBaseDir+"/pat/PATtuple_176_1_Ffj.root",
  sampleBaseDir+"/pat/PATtuple_177_1_dXr.root",
  sampleBaseDir+"/pat/PATtuple_178_1_TGL.root",
  sampleBaseDir+"/pat/PATtuple_179_1_lff.root",
  sampleBaseDir+"/pat/PATtuple_180_1_NPa.root",
  sampleBaseDir+"/pat/PATtuple_181_1_Ir9.root",
  sampleBaseDir+"/pat/PATtuple_182_1_blz.root",
  sampleBaseDir+"/pat/PATtuple_183_1_Uvw.root",
  sampleBaseDir+"/pat/PATtuple_184_1_Ekq.root",
  sampleBaseDir+"/pat/PATtuple_185_1_igs.root",
  sampleBaseDir+"/pat/PATtuple_186_1_zTx.root",
  sampleBaseDir+"/pat/PATtuple_187_1_yX1.root",
  sampleBaseDir+"/pat/PATtuple_188_1_f4m.root",
  sampleBaseDir+"/pat/PATtuple_189_1_TW6.root",
  sampleBaseDir+"/pat/PATtuple_190_2_we3.root",
  sampleBaseDir+"/pat/PATtuple_191_1_QiR.root",
  sampleBaseDir+"/pat/PATtuple_192_1_QpC.root",
  sampleBaseDir+"/pat/PATtuple_193_1_mHA.root",
  sampleBaseDir+"/pat/PATtuple_194_1_xLz.root",
  sampleBaseDir+"/pat/PATtuple_195_1_NI6.root",
  sampleBaseDir+"/pat/PATtuple_196_1_1gl.root",
  sampleBaseDir+"/pat/PATtuple_197_2_uO3.root",
  sampleBaseDir+"/pat/PATtuple_198_1_cJB.root",
  sampleBaseDir+"/pat/PATtuple_199_2_IUR.root",
  sampleBaseDir+"/pat/PATtuple_200_1_3FZ.root",
  sampleBaseDir+"/pat/PATtuple_201_1_q8G.root",
  sampleBaseDir+"/pat/PATtuple_202_1_Qo9.root",
  sampleBaseDir+"/pat/PATtuple_203_2_LE8.root",
  sampleBaseDir+"/pat/PATtuple_204_2_LMm.root",
  sampleBaseDir+"/pat/PATtuple_205_1_FGp.root",
  sampleBaseDir+"/pat/PATtuple_206_1_Rnr.root",
  sampleBaseDir+"/pat/PATtuple_207_1_YOT.root",
  sampleBaseDir+"/pat/PATtuple_208_1_8q9.root",
  sampleBaseDir+"/pat/PATtuple_209_1_PmB.root",
  sampleBaseDir+"/pat/PATtuple_210_1_MmF.root"
]

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "MC"
sampleRunMu = 0
