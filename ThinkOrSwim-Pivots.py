#hint: Just Testing

#BaoPivots (Floor Pivots) with R4, S4
#Author @kphuynh82

#input aggregationPeriod = AggregationPeriod.DAY;
#input showOnlyToday = yes;

def aggregationPeriod = AggregationPeriod.DAY;
def PH = high(period = AggregationPeriod.DAY)[1];
def PL = low(period = AggregationPeriod.DAY)[1];
def PC = close(period = AggregationPeriod.DAY)[1];
def PPP;
def RR1;
def RR2;
def RR3;
def RR4; 
def SS1;
def SS2;
def SS3;
def SS4;

plot R4 = HighestAll(RR4);
plot R3 = HighestAll(RR3);
plot R2 = HighestAll(RR2);
plot R1 = HighestAll(RR1);
plot PP = HighestAll(PPP);
plot S1 = HighestAll(SS1);
plot S2 = HighestAll(SS2);
plot S3 = HighestAll(SS3);
plot S4 = HighestAll(SS4);

#if showOnlyToday and !IsNaN(close(period = aggregationPeriod)[-1])
if !IsNaN(close(period = aggregationPeriod)[-1])
then {
  
    RR1 = Double.NaN;
    RR2 = Double.NaN;
    RR3 = Double.NaN;
    RR4 = Double.NaN;
    PPP = Double.NaN;
    SS1 = Double.NaN;
    SS2 = Double.NaN;
    SS3 = Double.NaN;
    SS4 = Double.NaN;

} else {

    PPP = (PH + PL + PC) / 3;
    RR1 = 2 * PPP - PL;
    RR2 = PPP + (PH - PL);
    RR3 = 2 * PPP + (PH - 2 * PL);
    RR4 = PH + 3 * (PPP - PL);
    SS1 = 2 * PPP - PH;
    SS2 = PPP - (PH - PL);
    SS3 = 2 * PPP - (2 * PH - PL);
    SS4 = PL - 3 * (PH - PPP);
}


R4.SetDefaultColor(GetColor(5));
R3.SetDefaultColor(GetColor(5));
R2.SetDefaultColor(GetColor(5));
R1.SetDefaultColor(GetColor(5));
PP.SetDefaultColor(GetColor(0));
S1.SetDefaultColor(GetColor(6));
S2.SetDefaultColor(GetColor(6));
S3.SetDefaultColor(GetColor(6));
S4.SetDefaultColor(GetColor(6));

R4.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
PP.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S4.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);