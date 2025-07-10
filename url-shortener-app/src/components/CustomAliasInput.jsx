import React from 'react';

export default function CustomAliasInput({ value, onChange }) {
  return (
    <div className="mb-3">
      <label htmlFor="customAlias" className="form-label text-muted">
        Custom alias (optional)
      </label>
      <input
        type="text"
        id="customAlias"
        className="form-control form-control-lg"
        placeholder="e.g. my-custom-link"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
