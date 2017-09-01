#include "TH1F.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFile.h"
#include "THStack.h"

void Detector_Changes_Histograms()
{
    double L = 5000.; //Integrated luminosity in inverse fb
    double Xsec_HZ_BR_Hgamgam = 0.4; //Cross-section * BR in fb
    double N_Exp_Signal = L * Xsec_HZ_BR_Hgamgam;
    double N_Gen_Signal = 39361.;
    double Signal_Hist_Scale_Factor = N_Exp_Signal / N_Gen_Signal;

    TFile * Signal_File = new TFile("OutDir_1/ee_ZH_Z_Hgamgam_4/heppy.analyzers.examples.zh_hgamgam.TreeProducer.TreeProducer_1/tree.root", "Read");
    
    TTree * Signal_Tree = (TTree*)Signal_File->Get("events");

    TH1F * Signal_Higgs_Mass_Hist = new TH1F("Signal_Higgs_Mass", "Mass of reconstructed Higgs particles", 60, 110, 140);

    Signal_Higgs_Mass_Hist->Sumw2();

    Signal_Tree->SetBranchStatus("*", 0);
    Signal_Tree->SetBranchStatus("higgs_m", 1);

    double Signal_Higgs_Mass;

    Signal_Tree->SetBranchAddress("higgs_m", &Signal_Higgs_Mass);

    for (int Higgs_Number = 0; Higgs_Number < Signal_Tree->GetEntries(); ++ Higgs_Number)
    {
        Signal_Tree->GetEntry(Higgs_Number);
        Signal_Higgs_Mass_Hist->Fill(Signal_Higgs_Mass);
    }

    Signal_Higgs_Mass_Hist->Scale(Signal_Hist_Scale_Factor);

    TCanvas * c1 = new TCanvas("c1", "Higgs reconstruction histograms", 800, 600);
    gStyle->SetOptStat(0);
    gStyle->SetOptFit();
   
    Signal_Higgs_Mass_Hist->SetLineColor(kBlue);
    Signal_Higgs_Mass_Hist->SetLineWidth(3);
    Signal_Higgs_Mass_Hist->Draw("hist");
    Signal_Higgs_Mass_Hist->Draw("func same");
    Signal_Higgs_Mass_Hist->SetAxisRange(0., 300.,"Y");
    Signal_Higgs_Mass_Hist->GetXaxis()->SetTitle("Higgs Mass/GeV");
    Signal_Higgs_Mass_Hist->GetYaxis()->SetTitle("Number of events/500 MeV");
    Signal_Higgs_Mass_Hist->SetTitle("CMS Detector");
   Signal_Higgs_Mass_Hist->GetYaxis()->SetTitleOffset(1.4);
    Signal_Higgs_Mass_Hist->Fit("gaus");

    TLegend * Mass_Legend = new TLegend(0.15,0.8,0.25,0.9);
    Mass_Legend->SetHeader("Mass histogram legend");
    Mass_Legend->AddEntry(Signal_Higgs_Mass_Hist, "Signal Histogram", "l");
    Mass_Legend->Draw();

    c1->Update();
    c1->Draw();
    c1->Print("CMS_Detector.pdf");
    return;
}
