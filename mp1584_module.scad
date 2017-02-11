$fn = 50;

w = 22.098;
h = 16.764;

module pin() {
    cylinder(h=2, r=1);
}

module pcb() {
    difference() {
        cube([22.098, 16.764, 1.2]);
        
        translate([1.778, 1.778]) pin();
        translate([w-1.778, 1.778]) pin();
        translate([w-1.778, h-1.778]) pin();
        translate([1.778, h-1.778]) pin();
        
        translate([1.778, 4.318]) pin();
        translate([w-1.778, 4.318]) pin();
        translate([w-1.778, h-4.318]) pin();
        translate([1.778, h-4.318]) pin();
    }
}

module parts() {
    translate([13, 9, 0])
        cube([5, 5, 2.8]);
    translate([7, 7.5, 0])
        cube([5, 3, 1.5]);
    translate([1, 6.4, 0])
        cube([1.5, 4, 1.5]);
    translate([19.5, 6.4, 0])
        cube([1.5, 4, 1.5]);
}

pcb();
translate([0, 0, 1.2]) parts();