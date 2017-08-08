from ROOT import TTree
from ROOT import TH1F
from ROOT import TFile
from ROOT import TCanvas
from ROOT import TBranch

Tree_File = TFile("OutDir/ee_ZH_Z_Hgamgam_2/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read")
Tree = Tree_File.Get("events;1")

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

higgs_mass = 0.0
higgs_eta = 0.0
higgs_phi = 0.0
lead_photon_pt = 0.0
sub_lead_photon_pt = 0.0

Tree.SetBranchAddress("higgs_m", higgs_mass)
Tree.SetBranchAddress("higgs_eta", higgs_eta)
Tree.SetBranchAddress("higgs_phi", higgs_phi)
Tree.SetBranchAddress("photon1_pt", lead_photon_pt)
Tree.SetBranchAddress("photon2_pt", sub_lead_photon_pt)

for higgs_number in range(Tree.GetEntries()):
    Tree.GetEntry(higgs_number)
    higgs_mass_hist.Fill(higgs_mass)
    higgs_eta_hist.Fill(higgs_eta)
    higgs_phi_hist.Fill(higgs_phi)
    lead_photon_pt_hist.Fill(lead_photon_pt)
    sub_lead_photon_pt_hist.Fill(sub_lead_photon_pt)

c1 = TCanvas("c1", "Higgs and leading photon histograms", 800, 600)
c1.Divide(3,2,0,0)

c1.cd(1)
higgs_mass_hist.Draw()

c1.cd(2)
higgs_eta_hist.Draw()

c1.cd(3)
higgs_phi_hist.Draw()

c1.cd(4)
lead_photon_pt_hist.Draw()

c1.cd(5)
sub_lead_photon_pt_hist.Draw()

c1.Update()
c1.Draw()
