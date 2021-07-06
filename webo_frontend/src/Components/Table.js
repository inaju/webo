import * as React from "react";
import { DataGrid } from "@material-ui/data-grid";

const columns = [
  { field: "id", headerName: "ID", width: 70 },
  { field: "firstName", headerName: "First name", width: 130 },
  { field: "lastName", headerName: "Last name", width: 130 },
  {
    field: "age",
    headerName: "Age",
    type: "number",
    width: 90,
  },

  {
    field: "fullName",
    headerName: "Full name",
    description: "This column has a value getter and is not sortable.",
    sortable: false,
    width: 160,
    // valueGetter: (params) =>
    //   `${params.getValue('firstName') || ''} ${params.getValue('lastName') || ''}`,
  },
];

const rows = [
  { id: 1, lastName: "Snow", firstName: "Jon", age: 35 },
  { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
  { id: 3, lastName: "Lannister", firstName: "Jaime", age: 45 },
  { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
  { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
  { id: 6, lastName: "Melisandre", firstName: null, age: 150 },
  { id: 7, lastName: "Clifford", firstName: "Ferrara", age: 44 },
  { id: 8, lastName: "Frances", firstName: "Rossini", age: 36 },
  { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65 },
];

export default function DataTable() {
  return (
    <div style={{ height: 400, width: "100%" }}>
      <DataGrid rows={rows} columns={columns} pageSize={10} checkboxSelection />
    </div>
  );
}

// import React from 'react'
// import Griddle, { plugins } from 'griddle-react';

// function Table() {
//   const NewLayout = ({ Table, Pagination, Filter, SettingsWrapper }) => (
//     <div>
//       <Filter />
//       <Pagination />
//       <Table />
//     </div>
//   );
//     var data = [
//         {
//           "id": 1,
//           "name": "Mayer Leonard",
//           "city": "Kapowsin",
//           "state": "Hawaii",
//           "country": "United Kingdom",
//           "company": "Ovolo",
//           "favoriteNumber": 7
//         },
//         {
//             "id": 2,
//             "name": "Mitchel Inaju",
//             "city": "Kapowsin",
//             "state": "Hawaii",
//             "country": "United Kingdom",
//             "company": "Ovolo",
//             "favoriteNumber": 7
//           },
//           {
//             "id": 3,
//             "name": "John Inaju",
//             "city": "Kapowsin",
//             "state": "Hawaii",
//             "country": "United Kingdom",
//             "company": "Ovolo",
//             "favoriteNumber": 7
//           },
//           {
//             "id": 4,
//             "name": "Moses Tobi",
//             "city": "Kapowsin",
//             "state": "Hawaii",
//             "country": "United Kingdom",
//             "company": "Ovolo",
//             "favoriteNumber": 7
//           },

//       ];
//     return (
//         <div className="table-component">
//             <Griddle
//                 data={data}
//                 plugins={[plugins.LocalPlugin]}
//                 components={{
//                     Layout: NewLayout
//                 }}
//             />
//         </div>
//     )

// }

// export default Table
