#include "TH1F.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"
#include "THStack.h"

void Mass_Histograms_TEST()
{
    double L = 5000.; //Integrated luminosity in inverse fb
    double Xsec_HZ_BR_Hgamgam = 0.4; //Cross-section * BR in fb - leading order only
    double N_Exp_Signal = L * Xsec_HZ_BR_Hgamgam;
    double N_Gen_Signal = 39361.;
    double Signal_Hist_Scale_Factor = N_Exp_Signal / N_Gen_Signal;
    double Xsec_Zgam = 26460.; //Leading order only
    double N_Exp_Full_Background = L * Xsec_Zgam;
    double N_Gen_Full_Background = 1000000.;
    double Full_Background_Hist_Scale_Factor = N_Exp_Full_Background / N_Gen_Full_Background;
    double Xsec_Zgam_BR_hadronic = Xsec_Zgam*0.6991;
    double N_Exp_Hadronic_Background = L * Xsec_Zgam_BR_hadronic;
    double N_Gen_Hadronic_Background = 1000000.;
    double Hadronic_Background_Hist_Scale_Factor = N_Exp_Hadronic_Background / N_Gen_Hadronic_Background;

    TFile * Signal_File = new TFile("OutDir_1/ee_ZH_Z_Hgamgam_2/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");
    TFile * Full_Background_File = new TFile("/afs/cern.ch/work/e/eljones/public/FCCSamples/OutDir_full_background_1M/ee_Zgam_full_1/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");
//    TFile * Hadronic_Background_File = new TFile("/afs/cern.ch/work/e/eljones/public/FCCSamples/OutDir_hadronic_background_1M/ee_Zgam_hadronic/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");

    TTree * Signal_Tree = (TTree*)Signal_File->Get("events");
    TTree * Full_Background_Tree = (TTree*)Full_Background_File->Get("events");
//    TTree * Hadronic_Background_Tree = (TTree*)Hadronic_Background_File->Get("events");

    TH1F * Signal_Higgs_Mass_Hist = new TH1F("Signal_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110, 140);
    TH1F * Full_Background_Higgs_Mass_Hist = new TH1F("Full_Background_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110, 140);
//    TH1F * Hadronic_Background_Higgs_Mass_Hist = new TH1F("Hadronic_Background_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110, 140);

    Signal_Tree->SetBranchStatus("*", 0);
    Signal_Tree->SetBranchStatus("higgs_m", 1);
    Full_Background_Tree->SetBranchStatus("*", 0);
    Full_Background_Tree->SetBranchStatus("higgs_m", 1);
//    Hadronic_Background_Tree->SetBranchStatus("*", 0);
//    Hadronic_Background_Tree->SetBranchStatus("higgs_m", 1);

    double Signal_Higgs_Mass;
    double Full_Background_Higgs_Mass;
//    double Hadronic_Background_Higgs_Mass;

    Signal_Tree->SetBranchAddress("higgs_m", &Signal_Higgs_Mass);
    Full_Background_Tree->SetBranchAddress("higgs_m", &Full_Background_Higgs_Mass);
//    Hadronic_Background_Tree->SetBranchAddress("higgs_m", &Hadronic_Background_Higgs_Mass);

    for (int Higgs_Number = 0; Higgs_Number < Signal_Tree->GetEntries(); ++ Higgs_Number)
    {
        Signal_Tree->GetEntry(Higgs_Number);
        Signal_Higgs_Mass_Hist->Fill(Signal_Higgs_Mass);
    }
    for (int Higgs_Number = 0; Higgs_Number < Full_Background_Tree->GetEntries(); ++ Higgs_Number)
    {
        Full_Background_Tree->GetEntry(Higgs_Number);
        Full_Background_Higgs_Mass_Hist->Fill(Full_Background_Higgs_Mass);
    }
//    for (int Higgs_Number = 0; Higgs_Number < Hadronic_Background_Tree->GetEntries(); ++ Higgs_Number)
//    {
//        Hadronic_Background_Tree->GetEntry(Higgs_Number);
//        Hadronic_Background_Higgs_Mass_Hist->Fill(Hadronic_Background_Higgs_Mass);
//    }

    Signal_Higgs_Mass_Hist->Scale(Signal_Hist_Scale_Factor);
    Full_Background_Higgs_Mass_Hist->Scale(Full_Background_Hist_Scale_Factor);
//    Hadronic_Background_Higgs_Mass_Hist->Scale(Hadronic_Background_Hist_Scale_Factor);

    TCanvas * c1 = new TCanvas("c1", "Higgs reconstruction histograms", 800, 600);
    gStyle->SetOptStat(0);
//    gStyle->SetOptFit();

    TF1 * gaus_plus_pol1 = new TF1("gaus_plus_pol1", "[0]*exp(-0.5*((x-[1])/[2])^2) + [3] + [4]*x", 110, 140);
    gaus_plus_pol1->SetParameter(0, 3700);
    gaus_plus_pol1->SetParameter(1, 125.1);
    gaus_plus_pol1->SetParameter(2, 1.600);
    gaus_plus_pol1->SetParLimits(0, 0, 6000);
    gaus_plus_pol1->SetParLimits(1, 120, 130);
    gaus_plus_pol1->SetParLimits(2, 0.2, 2);

    TH1F * Signal_Hist = new TH1F("Signal_Plus_Background_Higgs_Mass", "Mass of reconstructed Higgs particles", 15, 110,140);
    Signal_Hist->Add(Signal_Higgs_Mass_Hist);
    Signal_Hist->Add(Full_Background_Higgs_Mass_Hist);
    Signal_Hist->Sumw2();
    Signal_Hist->SetLineColor(kMagenta);
    Signal_Hist->SetLineWidth(3);
    Signal_Hist->SetAxisRange(0., 6000., "Y");
    Signal_Hist->GetXaxis()->SetTitle("Higgs Mass / GeV");
    Signal_Hist->GetYaxis()->SetTitle("Number of events / 2 GeV");
    Signal_Hist->GetYaxis()->SetTitleOffset(1.4);
    Signal_Hist->Fit("gaus_plus_pol1");
    Signal_Hist->Draw("func");

    Full_Background_Higgs_Mass_Hist->SetFillStyle(3003);
    Full_Background_Higgs_Mass_Hist->SetFillColorAlpha(4, 0.1);
    Full_Background_Higgs_Mass_Hist->SetLineWidth(3);
    Full_Background_Higgs_Mass_Hist->SetAxisRange(0., 6000., "Y");
    Full_Background_Higgs_Mass_Hist->Sumw2();
    Full_Background_Higgs_Mass_Hist->Draw("same hist");

//    Hadronic_Background_Higgs_Mass_Hist->SetLineColor(kBlack);
//    Hadronic_Background_Higgs_Mass_Hist->SetLineWidth(3);
//    Hadronic_Background_Higgs_Mass_Hist->SetAxisRange(0., 6000., "Y");
//    Hadronic_Background_Higgs_Mass_Hist->Sumw2();
//    Hadronic_Background_Higgs_Mass_Hist->Draw("same hist");

    TLegend * Mass_Legend = new TLegend(0.15,0.8,0.25,0.9);
    Mass_Legend->AddEntry(Signal_Hist, "Signal", "l");
    Mass_Legend->AddEntry(Full_Background_Higgs_Mass_Hist, "All backgrounds", "f");
//    Mass_Legend->AddEntry(Hadronic_Background_Higgs_Mass_Hist, "Z->qqbar", "f");
    Mass_Legend->Draw();

    c1->Update();
    c1->Draw();
    c1->Print("Signal_Plus_Background.pdf");

    return;
}
