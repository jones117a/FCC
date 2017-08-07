from ROOT import TTree
from ROOT import TH1F

Tree = TTree("OutDir/ee_ZH_Z_Hgamgam_2/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read")
higgs_mass_hist = TH1F("higgs_mass", "Mass of reconstructed Higgs particles", 2000, 0, 200)
higgs_eta_hist = TH1F("higgs_eta", "Pseudorapidity of reconstructed Higgs particles", 200, 0, 20)
higgs_phi_hist = TH1F("higgs_phi", "Angle of reconstructed Higgs particles from beam axis", 200, 0, 20)
lead_photon_pt_hist = TH1F("lead_photon_pt_hist", "Pt of leading photon in event", 200, 0, 20)
sub_lead_photon_pt_hist = TH1F("sub_lead_photon_pt_hist", "Pt of sub-leading photon in event", 200, 0, 20)

Tree.SetBranchStatus("*", 0)
Tree.SetBranchStatus("higgs_m", 1)
Tree.SetBranchStatus("higgs_eta", 1)
Tree.SetBranchStatus("higgs_phi", 1)
Tree.SetBranchStatus("photon1_pt", 1)
Tree.SetBranchStatus("photon2_pt", 1)

Tree.SetBranchAddress("higgs_m", higgs_mass)
Tree.SetBranchAddress("higgs_eta", higgs_eta)
Tree.SetBranchAddress("higgs_phi", higgs_phi)
Tree.SetBranchAddress("photon1_pt", lead_photon_pt)
Tree.SetBranchAddress("photon2_pt", sub_lead_photon_pt)

for higgs_number in Tree.GetEntries():
    Tree.GetEntry(higgs_number)
    higgs_mass_hist.Fill(higgs_mass)
    higgs_eta_hist.Fill(higgs_eta)
    higgs_phi_hist.Fill(higgs_phi)
    lead_photon_pt_hist.Fill(lead_photon_pt)
    sub_lead_photon_pt_hist.Fill(sub_lead_photon_pt)

Tree.Draw("higgs_m")
Tree.Draw("higgs_eta")
Tree.Draw("higgs_phi")
Tree.Draw("lead_photon_pt")
Tree.Draw("sub_lead_photon_pt") 
