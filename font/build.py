#!/usr/bin/env python2

import fontforge;
import psMat;

import string;

def create(font):
    for cp in range(0x0020, 0x007b):
        font.createChar(cp);

    font.addLookup("compose-1", "gsub_ligature", (), (("ccmp", (("DFLT", ("dflt")), ("latn", ("dflt")))),));
    font.addLookupSubtable("compose-1", "compose-1-1");

    font.addLookup("singlesub-1", "gsub_single", (), (("", (("DFLT", ("dflt")), ("latn", ("dflt")))),));
    font.addLookupSubtable("singlesub-1", "singlesub-1-1");
    
    
    #punctuations
    font["space"].width = 200;
    font["exclam"].importOutlines("./glyphs/excl.svg");
    font["comma"].importOutlines("./glyphs/comma.svg");
    font["period"].importOutlines("./glyphs/period.svg");
    font["question"].importOutlines("./glyphs/ques.svg");

    
    #numerals
    for i in range(0,10):
        font[0x0030 + i].importOutlines("./glyphs/%s.svg" % i);
    

    #vowels
    font["a"].importOutlines("./glyphs/a.svg");
    font["i"].importOutlines("./glyphs/i.svg");
    font["u"].importOutlines("./glyphs/u.svg");
    font["e"].importOutlines("./glyphs/e.svg");
    font["o"].importOutlines("./glyphs/o.svg");
    font["y"].importOutlines("./glyphs/y.svg");

    font["A"].importOutlines("./glyphs/a.svg");
    font["I"].importOutlines("./glyphs/i.svg");
    font["U"].importOutlines("./glyphs/u.svg");
    font["E"].importOutlines("./glyphs/e.svg");
    font["O"].importOutlines("./glyphs/o.svg");
    font["Y"].importOutlines("./glyphs/y.svg");

    #consonants
    font["p"].importOutlines("./glyphs/p.svg");
    font["P"].importOutlines("./glyphs/p.svg");

    font["f"].importOutlines("./glyphs/f.svg");
    font["F"].importOutlines("./glyphs/f.svg");
    
    font["t"].importOutlines("./glyphs/t.svg")
    font["T"].importOutlines("./glyphs/t.svg");

    font["c"].importOutlines("./glyphs/c.svg");
    font["C"].importOutlines("./glyphs/c.svg");

    font["x"].importOutlines("./glyphs/x.svg");
    font["X"].importOutlines("./glyphs/x.svg");
    
    font["k"].importOutlines("./glyphs/k.svg");
    font["K"].importOutlines("./glyphs/k.svg");
    
    font["q"].importOutlines("./glyphs/q.svg");
    font["Q"].importOutlines("./glyphs/q.svg");

    font["h"].importOutlines("./glyphs/h.svg");
    font["H"].importOutlines("./glyphs/h.svg");

    font["r"].importOutlines("./glyphs/r.svg");
    font["R"].importOutlines("./glyphs/r.svg");

    font["z"].importOutlines("./glyphs/z.svg");
    font["Z"].importOutlines("./glyphs/z.svg");

    font["m"].importOutlines("./glyphs/m.svg");
    font["M"].importOutlines("./glyphs/m.svg");
    
    font["n"].importOutlines("./glyphs/n.svg");
    font["N"].importOutlines("./glyphs/n.svg");

    font["l"].importOutlines("./glyphs/l.svg");
    font["L"].importOutlines("./glyphs/l.svg");
    
    font["j"].importOutlines("./glyphs/j.svg");
    font["J"].importOutlines("./glyphs/j.svg");

    font["w"].importOutlines("./glyphs/w.svg");
    font["W"].importOutlines("./glyphs/w.svg");

    font["b"].importOutlines("./glyphs/b.svg");
    font["B"].importOutlines("./glyphs/b.svg");

    font["v"].importOutlines("./glyphs/v.svg");
    font["V"].importOutlines("./glyphs/v.svg");

    font["d"].importOutlines("./glyphs/d.svg");
    font["D"].importOutlines("./glyphs/d.svg");

    font["s"].importOutlines("./glyphs/s.svg");
    font["S"].importOutlines("./glyphs/s.svg");
    
    font["g"].importOutlines("./glyphs/g.svg");
    font["G"].importOutlines("./glyphs/g.svg");

    
    font.createChar(-1, "lipa-fh");
    font["lipa-fh"].importOutlines("./glyphs/fh.svg");
    font["lipa-fh"].addPosSub("compose-1-1", ("f", "h"));
    font["lipa-fh"].addPosSub("compose-1-1", ("f", "H"));
    font["lipa-fh"].addPosSub("compose-1-1", ("F", "h"));
    font["lipa-fh"].addPosSub("compose-1-1", ("F", "H"));
    
    font.createChar(-1, "lipa-vh");
    font["lipa-vh"].importOutlines("./glyphs/vh.svg");
    font["lipa-vh"].addPosSub("compose-1-1", ("v", "h"));
    font["lipa-vh"].addPosSub("compose-1-1", ("v", "H"));
    font["lipa-vh"].addPosSub("compose-1-1", ("V", "h"));
    font["lipa-vh"].addPosSub("compose-1-1", ("V", "H"));
    
    font.createChar(-1, "lipa-dz");
    font["lipa-dz"].importOutlines("./glyphs/dz.svg");
    font["lipa-dz"].addPosSub("compose-1-1", ("d", "z"));
    font["lipa-dz"].addPosSub("compose-1-1", ("d", "Z"));
    font["lipa-dz"].addPosSub("compose-1-1", ("D", "z"));
    font["lipa-dz"].addPosSub("compose-1-1", ("D", "Z"));

    font.createChar(-1, "lipa-long-r");
    font["lipa-long-r"].importOutlines("./glyphs/long_r.svg");
    font["r"].addPosSub("singlesub-1-1", "lipa-long-r");
    
    font.addLookup("contextual-1", "gsub_contextchain", (), (("calt", (("DFLT", ("dflt")), ("latn", ("dflt")))),));
    font.addContextualSubtable("contextual-1", "contextual-1-1", "coverage", "[a i u e o y] | [r]@<singlesub-1>")

    

    font["quotesingle"].importOutlines("./glyphs/apos.svg");

    for cp in list(string.ascii_letters) + ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + ["lipa-fh", "lipa-vh", "lipa-dz", "lipa-long-r"] + ["exclam", "comma", "period", "question", "quotesingle"]:
        if cp in font:
            font[cp].left_side_bearing = 50;
            font[cp].right_side_bearing = 50;


def main():
    font = fontforge.font();

    name = "liparxe-round";
    font.encoding = "UnicodeBmp";
    font.familyname = name;
    font.fullname = name;
    font.fontname = name;

    create(font);

    font.save("%s.sfd" % name);
    font.generate("%s.ttf" % name);
    

main();


