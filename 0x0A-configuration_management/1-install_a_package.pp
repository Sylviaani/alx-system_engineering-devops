#installing a package

exec { 'pkill' :
command  => 'pkill killmenow',
provider => 'shell',
}
