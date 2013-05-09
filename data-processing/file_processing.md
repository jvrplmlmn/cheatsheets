### Remove empty lines from file

#### grep

    grep . FILE

#### awk

    awk /./{print} FILE

#### sed

    sed -e /^$/d FILE
